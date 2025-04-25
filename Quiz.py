import json
import random
import time

def load_questions(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
    except UnicodeDecodeError:
        with open(path, 'r', encoding='latin-1') as file:
            questions = json.load(file)
    except json.JSONDecodeError:
        print("Error reading the JSON file. Please check its format and content.")
        questions = []
    return questions

def quiz(questions):
    score = 0
    if not questions:
        print("No questions available.")
        return

    while True:
        try:
            num_questions = int(input("Would you like to do a quiz of 10 or 20 questions? Enter 10 or 20: "))
            if num_questions in (10, 20) and num_questions <= len(questions):
                break
            else:
                print(f"Please enter either 10 or 20. There are {len(questions)} questions available.")
        except ValueError:
            print("That's not a valid number.")

    selected_questions = random.sample(questions, num_questions)

    for i, question in enumerate(selected_questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        options = question['options']
        if isinstance(options, dict):
            for key, value in options.items():
                print(f"{key}. {value}")
        else:
            for index, option in enumerate(options):
                print(f"{chr(65 + index)}. {option}")

        user_input = input("Enter your answer(s) separated by commas (e.g., A,B): ")
        user_answers = [ans.strip().upper() for ans in user_input.split(',')]
        correct_answers = question['answer'] if isinstance(question['answer'], list) else [question['answer']]

        if set(user_answers) == set(correct_answers):
            print(f"Correct! {question.get('feedback', 'No additional explanation provided.')}")
            score += 1
        else:
            if isinstance(options, dict):
                correct_text = ', '.join(options[ans] for ans in correct_answers)
            else:
                correct_text = ', '.join(options[ord(ans) - 65] for ans in correct_answers)
            print(f"Incorrect. The correct answer(s): {correct_text}. {question.get('feedback', 'No additional explanation provided.')}")
        
        time.sleep(2)
    
    print(f"\nYou scored {score}/{num_questions} ({score/num_questions * 100:.2f}%).")

def main():
    path = 'quizes\network_quiz.json'  # Ensure this matches your quiz JSON file
    questions = load_questions(path)
    if questions:
        quiz(questions)
        while input("Would you like to retake the quiz? (yes/no): ").strip().lower() in ('yes', 'y'):
            quiz(questions)
        print("Thank you for participating!")

if __name__ == "__main__":
    main()
