from flask import Flask, render_template

app = Flask(__name__)

questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is the square of 5?",
        "options": ["10", "15", "20", "25"],
        "answer": "25"
    },
    {
        "question": "What is 10 × 3?",
        "options": ["13", "20", "30", "40"],
        "answer": "30"
    },
    {
        "question": "What is the value of 100 ÷ 10?",
        "options": ["5", "10", "20", "50"],
        "answer": "10"
    },
    {
        "question": "Which number is a prime number?",
        "options": ["4", "6", "9", "7"],
        "answer": "7"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True)