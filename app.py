from flask import Flask, jsonify, request, send_from_directory, render_template  # Import render_template
from flask_cors import CORS  # Import CORS
import json
import random


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load questions from JSON file
with open('quizes/network_quiz.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

@app.route('/')
def index():
    return render_template('quiz.html')  # Serve the quiz.html file from the templates folder

@app.route('/get-questions', methods=['GET'])
def get_questions():
    num_questions = int(request.args.get('num_questions', 10))  # Default to 10 questions
    selected_questions = random.sample(questions, num_questions)
    return jsonify(selected_questions)

@app.route('/submit-answers', methods=['POST'])
def submit_answers():
    data = request.json
    user_answers = data.get('answers', [])
    correct_count = 0
    total_questions = len(user_answers)
    
    for answer in user_answers:
        if set(answer['user_answers']) == set(answer['correct_answers']):
            correct_count += 1

    return jsonify({
        "score": correct_count,
        "total": total_questions,
        "percentage": (correct_count / total_questions) * 100
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
