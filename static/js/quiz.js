let questions = [];
let currentQuestionIndex = 0;
let userAnswers = [];
let score = 0;

async function loadQuestions() {
    const quizType = window.selectedQuiz || 'network';
    const resp = await fetch(`/get-questions?num_questions=10&quiz=${quizType}`);
    questions = await resp.json();
    displayQuestion();
}

function displayQuestion() {
    const questionArea = document.getElementById('question-area');
    const feedbackArea = document.getElementById('feedback-area');
    const q = questions[currentQuestionIndex];

    questionArea.innerHTML = `
        <div class="question">
            <h2>${currentQuestionIndex+1}. ${q.question}</h2>
            ${Object.keys(q.options).map(key=>`
                <label>
                  <input type="checkbox" name="answer" value="${key}">
                  ${key}. ${q.options[key]}
                </label>
            `).join('')}
        </div>
    `;
    feedbackArea.innerHTML = '';
    document.getElementById('submit-answer-btn').style.display = 'inline';
    document.getElementById('next-btn').style.display   = 'none';
}

document.getElementById('submit-answer-btn').addEventListener('click', handleAnswer);
document.getElementById('next-btn').addEventListener('click', ()=>{
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) displayQuestion();
    else showFinalScore();
});
document.getElementById('retry-btn').addEventListener('click', ()=>{
    currentQuestionIndex = 0;
    score = 0;
    userAnswers = [];
    document.getElementById('final-score').style.display   = 'none';
    document.getElementById('final-actions').style.display = 'none';
    document.getElementById('quiz-container').style.display= 'block';
    loadQuestions();
});

function handleAnswer() {
    const feedbackArea = document.getElementById('feedback-area');
    const q = questions[currentQuestionIndex];
    const selected = Array.from(
        document.querySelectorAll('input[name="answer"]:checked')
    ).map(i=>i.value);
    const correct = Array.isArray(q.answer) ? q.answer : [q.answer];
    const isCorrect = JSON.stringify(selected.sort()) === JSON.stringify(correct.sort());
    if (isCorrect) score++;
    const feedbackText = q.feedback || q.explanation || '';

    feedbackArea.innerHTML = `
    <div class="feedback ${isCorrect ? 'correct' : 'incorrect'}">
        ${!isCorrect && feedbackText ? `<p><strong>Explanation:</strong> ${feedbackText}</p>` : ''}
        <p><strong>Correct Answer:</strong> ${correct.join(', ')}</p>
    </div>
    `;

    document.getElementById('submit-answer-btn').style.display = 'none';
    document.getElementById('next-btn').style.display          = 'inline';
}

function showFinalScore() {
    document.getElementById('quiz-container').style.display = 'none';
    document.getElementById('final-score').style.display    = 'block';
    document.getElementById('final-actions').style.display  = 'flex';
    document.getElementById('final-score').innerHTML = `
      <p>You scored ${score}/${questions.length}</p>
      <p>That's ${(score / questions.length * 100).toFixed(2)}%!</p>
    `;
}

loadQuestions();
