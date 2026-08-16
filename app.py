from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random

app = Flask(__name__)

app.config["SECRET_KEY"] = "quiz-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =========================
# DATABASE MODELS
# =========================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(
        db.String(50),
        nullable=False
    )

    question = db.Column(
        db.String(500),
        nullable=False
    )

    option1 = db.Column(
        db.String(200),
        nullable=False
    )

    option2 = db.Column(
        db.String(200),
        nullable=False
    )

    option3 = db.Column(
        db.String(200),
        nullable=False
    )

    option4 = db.Column(
        db.String(200),
        nullable=False
    )

    answer = db.Column(
        db.String(200),
        nullable=False
    )


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    score = db.Column(
        db.Integer,
        nullable=False
    )

    total = db.Column(
        db.Integer,
        nullable=False
    )


# =========================
# HOME
# =========================

@app.route("/")
def index():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


# =========================
# REGISTER
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            flash("Email already registered!")

            return redirect(
                url_for("register")
            )

        hashed_password = generate_password_hash(
            password
        )

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration successful! Please login."
        )

        return redirect(
            url_for("login")
        )

    return render_template("register.html")


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            session["user_id"] = user.id
            session["username"] = user.username
            session["email"] = user.email

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Invalid email or password!"
        )

    return render_template("login.html")


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("index")
    )


# =========================
# USER DASHBOARD
# =========================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(
            url_for("login")
        )

    user = User.query.get(
        session["user_id"]
    )

    results = Result.query.filter_by(
        username=session["username"]
    ).order_by(
        Result.id.desc()
    ).all()

    categories = db.session.query(
        Question.category
    ).distinct().all()

    categories = [
        category[0]
        for category in categories
    ]

    total_quizzes = len(results)

    if total_quizzes > 0:

        total_percentage = sum(
            (r.score / r.total) * 100
            for r in results
        )

        average_score = round(
            total_percentage / total_quizzes
        )

        best_score = max(
            round((r.score / r.total) * 100)
            for r in results
        )

    else:

        average_score = 0
        best_score = 0

    recent_results = results[:5]

    return render_template(
        "dashboard.html",
        user=user,
        categories=categories,
        total_quizzes=total_quizzes,
        average_score=average_score,
        best_score=best_score,
        recent_results=recent_results
    )


# =========================
# START QUIZ
# =========================

@app.route("/quiz/<category>")
def quiz(category):

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    questions = Question.query.filter_by(
        category=category
    ).all()

    random.shuffle(questions)

    questions = questions[:10]

    if not questions:

        flash(
            "No questions available!"
        )

        return redirect(
            url_for("dashboard")
        )

    session["quiz_questions"] = [
        q.id for q in questions
    ]

    return render_template(
        "quiz.html",
        questions=questions,
        category=category
    )


# =========================
# SUBMIT QUIZ
# =========================

@app.route(
    "/submit_quiz",
    methods=["POST"]
)
def submit_quiz():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    question_ids = session.get(
        "quiz_questions",
        []
    )

    score = 0

    review = []

    for question_id in question_ids:

        question = Question.query.get(
            question_id
        )

        selected = request.form.get(
            f"question_{question_id}"
        )

        if selected == question.answer:

            score += 1
            correct = True

        else:

            correct = False

        review.append({
            "question": question.question,
            "selected": selected,
            "correct_answer": question.answer,
            "correct": correct
        })

    category = request.form.get(
        "category"
    )

    result = Result(
        username=session["username"],
        category=category,
        score=score,
        total=len(question_ids)
    )

    db.session.add(result)
    db.session.commit()

    session["review"] = review

    return redirect(
        url_for(
            "result",
            score=score,
            total=len(question_ids)
        )
    )


# =========================
# RESULT
# =========================

@app.route(
    "/result/<int:score>/<int:total>"
)
def result(score, total):

    percentage = round(
        (score / total) * 100
    ) if total else 0

    review = session.get(
        "review",
        []
    )

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=percentage,
        review=review
    )


# =========================
# HISTORY
# =========================

@app.route("/history")
def history():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    results = Result.query.filter_by(
        username=session["username"]
    ).order_by(
        Result.id.desc()
    ).all()

    return render_template(
        "history.html",
        results=results
    )


# =========================
# ADMIN
# =========================

@app.route(
    "/admin",
    methods=["GET", "POST"]
)
def admin():

    if request.method == "POST":

        question = Question(

            category=request.form[
                "category"
            ],

            question=request.form[
                "question"
            ],

            option1=request.form[
                "option1"
            ],

            option2=request.form[
                "option2"
            ],

            option3=request.form[
                "option3"
            ],

            option4=request.form[
                "option4"
            ],

            answer=request.form[
                "answer"
            ]
        )

        db.session.add(question)

        db.session.commit()

        flash(
            "Question added successfully!"
        )

    questions = Question.query.all()

    return render_template(
        "admin.html",
        questions=questions
    )


# =========================
# CREATE DATABASE
# =========================

with app.app_context():

    db.create_all()


# =========================
# RUN
# =========================

if __name__ == "__main__":

    app.run(
        debug=True
    )