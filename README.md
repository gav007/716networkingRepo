📘 Network Quiz Web App
This project is a web-based multiple-choice quiz application built with Flask (Python backend) and HTML/CSS/JavaScript frontend. The app serves interactive quiz questions stored in a JSON file and provides feedback and scoring.

🧠 Features
✅ Multiple-choice quiz (single and multi-answer)
✅ Randomized question selection
✅ Score calculation with percentage
✅ Explanations for incorrect answers
✅ Responsive UI with stylish animations
✅ API routes for dynamic question delivery and answer submission
✅ CORS-enabled for frontend-backend communication

📁 Project Structure
bash
Copy
Edit
├── app.py                 # Flask backend server
├── index.html             # Frontend HTML + inline CSS & JS
├── network_quiz.json      # Quiz question bank (JSON format)
├── Quiz.py                # Standalone CLI-based quiz (Python)
🚀 Getting Started
1. Clone or Download the Project
bash
Copy
Edit
git clone https://github.com/your-username/network-quiz-app.git
cd network-quiz-app
2. Install Python Dependencies
Make sure Python 3.6+ is installed. Then install Flask:

bash
Copy
Edit
pip install flask flask-cors
3. Run the Flask Server
bash
Copy
Edit
python app.py
By default, it runs at http://localhost:5000.

4. Access the Quiz App
Open your browser and go to:
📎 http://localhost:5000

🔧 API Endpoints
GET /get-questions?num_questions=10
Returns a random selection of quiz questions.

Query Param: num_questions (default = 10)

Response: JSON list of questions with options and answers

POST /submit-answers
Submit answers and receive score feedback.

Request Body (JSON):

json
Copy
Edit
{
  "answers": [
    {
      "question": "Question text",
      "user_answers": ["A", "C"],
      "correct_answers": ["A", "C"]
    }
  ]
}
Response:

json
Copy
Edit
{
  "score": 8,
  "total": 10,
  "percentage": 80.0
}
🖥 CLI Mode (Optional)
You can also take the quiz via terminal using:

bash
Copy
Edit
python Quiz.py
Choose between 10 or 20 random questions, get instant feedback, and a final score summary.

📦 JSON Question Format
Each question in network_quiz.json follows:

json
Copy
Edit
{
  "type": "MC",
  "question": "What is an ISP?",
  "options": {
    "A": "Standard body",
    "B": "Protocol",
    "C": "Internet provider",
    "D": "Networking device"
  },
  "answer": "C",
  "feedback": "An ISP enables Internet access."
}
Multi-answer questions use answer: ["B", "D"].

🛠 Tech Stack
Backend: Python (Flask)

Frontend: HTML + CSS + Vanilla JavaScript

Data: JSON format

Extras: Flask-CORS, Responsive design, Local development only

📌 To Do (Optional Enhancements)
Store results in localStorage or backend

Add user login & progress tracking

Shuffle answers dynamically

Add difficulty levels

📃 License
MIT License – Free to use, adapt, and distribute.
