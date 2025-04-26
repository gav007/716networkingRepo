# validate_quizzes.py
import json, sys, os

QUIZ_DIR = os.path.join(os.path.dirname(__file__), 'quizes')
FILES = ["network_quiz.json","hardware_quiz.json","security_quiz.json","Questions_annotated.json"]

for name in FILES:
    path = os.path.join(QUIZ_DIR, name)
    try:
        with open(path, encoding='utf-8') as f:
            json.load(f)
        print(f"{name}: OK")
    except Exception as e:
        print(f"{name}: ERROR →", e)
        sys.exit(1)

print("All quiz JSON files are valid!")
