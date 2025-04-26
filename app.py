from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import json, random, numpy as np, matplotlib.pyplot as plt, os

app = Flask(__name__)
CORS(app)

QUIZ_FILES = {
    'network':    'quizes/network_quiz.json',
    'hardware':   'quizes/hardware_quiz.json',
    'security':   'quizes/security_quiz.json',
    'custom':     'quizes/Questions_annotated.json'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    # Pass quiz type into template
    return render_template('quiz.html',
                           selected_quiz=request.args.get('quiz', 'network'))

import os

@app.route('/get-questions')
def get_questions():
    qt   = request.args.get('quiz', 'network')
    rel  = QUIZ_FILES.get(qt)
    if not rel:
        return jsonify(error="Unknown quiz type"), 400

    # build absolute path
    full = os.path.join(app.root_path, rel)
    try:
        with open(full, encoding='utf-8') as f:
            questions = json.load(f)
    except Exception as e:
        return jsonify(error=f"Failed to load questions: {e}"), 500

    n = min(int(request.args.get('num_questions', 10)), len(questions))
    return jsonify(random.sample(questions, n))


@app.route('/opamp')
def opamp_form():
    return render_template('opamp.html')

@app.route('/simulate-opamp', methods=['POST'])
def simulate_opamp():
    # Read inputs
    rectifier_type = request.form['rectifier_type']
    vrms = float(request.form['vrms'])
    frequency = float(request.form['frequency'])
    diode_drop = float(request.form['diode_drop'])

    # Generate wave
    t = np.linspace(0, 1, 1000)
    input_wave = vrms * np.sqrt(2) * np.sin(2 * np.pi * frequency * t)

    if rectifier_type == "half":
        output_wave = np.maximum(0, input_wave - diode_drop)
    else:
        output_wave = np.maximum(0, np.abs(input_wave) - diode_drop)

    # Save plot
    os.makedirs('static/images', exist_ok=True)
    plt.figure(figsize=(10,6))
    plt.plot(t, input_wave, label="Input AC")
    plt.plot(t, output_wave, label=f"{rectifier_type.capitalize()}-Wave Rectified")
    plt.title("Rectifier Simulation")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.legend(); plt.grid(True)
    plt.savefig('static/images/rectifier_plot.png')
    plt.close()

    return render_template('opamp_result.html')

if __name__ == '__main__':
    app.run(debug=True)
