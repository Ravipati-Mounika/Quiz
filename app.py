from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import random

app = Flask(__name__)

app.config["SECRET_KEY"] = "quizmaster-secret-key"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(BASE_DIR, "quiz.db")
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =====================================================
# USER
# =====================================================

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(300),
        nullable=False
    )


# =====================================================
# QUESTION
# =====================================================

class Question(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(
        db.String(100),
        nullable=False
    )

    question = db.Column(
        db.Text,
        nullable=False
    )

    option1 = db.Column(
        db.String(300),
        nullable=False
    )

    option2 = db.Column(
        db.String(300),
        nullable=False
    )

    option3 = db.Column(
        db.String(300),
        nullable=False
    )

    option4 = db.Column(
        db.String(300),
        nullable=False
    )

    answer = db.Column(
        db.String(300),
        nullable=False
    )


# =====================================================
# RESULT
# =====================================================

class Result(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    category = db.Column(
        db.String(100),
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


# =====================================================
# QUESTIONS
# =====================================================

QUESTION_DATA = [

    # PYTHON

    {
        "category": "Python",
        "question": "Which keyword is used to define a function in Python?",
        "option1": "function",
        "option2": "def",
        "option3": "fun",
        "option4": "define",
        "answer": "def"
    },

    {
        "category": "Python",
        "question": "Which data type stores True or False?",
        "option1": "int",
        "option2": "str",
        "option3": "bool",
        "option4": "float",
        "answer": "bool"
    },

    {
        "category": "Python",
        "question": "Which symbol is used for comments?",
        "option1": "//",
        "option2": "#",
        "option3": "/*",
        "option4": "--",
        "answer": "#"
    },

    {
        "category": "Python",
        "question": "Which function finds the length of a list?",
        "option1": "length()",
        "option2": "size()",
        "option3": "len()",
        "option4": "count()",
        "answer": "len()"
    },

    {
        "category": "Python",
        "question": "Which collection is ordered and changeable?",
        "option1": "Tuple",
        "option2": "List",
        "option3": "Set",
        "option4": "FrozenSet",
        "answer": "List"
    },


    # JAVA

    {
        "category": "Java",
        "question": "Which keyword is used to create a class?",
        "option1": "class",
        "option2": "Class",
        "option3": "create",
        "option4": "newclass",
        "answer": "class"
    },

    {
        "category": "Java",
        "question": "Which method is the entry point of a Java program?",
        "option1": "start()",
        "option2": "run()",
        "option3": "main()",
        "option4": "execute()",
        "answer": "main()"
    },

    {
        "category": "Java",
        "question": "Which keyword is used for inheritance?",
        "option1": "inherit",
        "option2": "extends",
        "option3": "implements",
        "option4": "super",
        "answer": "extends"
    },

    {
        "category": "Java",
        "question": "Who originally developed Java?",
        "option1": "Microsoft",
        "option2": "Sun Microsystems",
        "option3": "Apple",
        "option4": "IBM",
        "answer": "Sun Microsystems"
    },

    {
        "category": "Java",
        "question": "Which symbol ends a Java statement?",
        "option1": ".",
        "option2": ":",
        "option3": ";",
        "option4": ",",
        "answer": ";"
    },


    # C

    {
        "category": "C",
        "question": "Who developed the C language?",
        "option1": "James Gosling",
        "option2": "Dennis Ritchie",
        "option3": "Bjarne Stroustrup",
        "option4": "Guido van Rossum",
        "answer": "Dennis Ritchie"
    },

    {
        "category": "C",
        "question": "Which function prints output in C?",
        "option1": "print()",
        "option2": "echo()",
        "option3": "printf()",
        "option4": "display()",
        "answer": "printf()"
    },

    {
        "category": "C",
        "question": "Which header file is required for printf()?",
        "option1": "stdlib.h",
        "option2": "stdio.h",
        "option3": "string.h",
        "option4": "math.h",
        "answer": "stdio.h"
    },

    {
        "category": "C",
        "question": "Which operator gets the address of a variable?",
        "option1": "*",
        "option2": "&",
        "option3": "#",
        "option4": "@",
        "answer": "&"
    },

    {
        "category": "C",
        "question": "Which loop executes at least once?",
        "option1": "for",
        "option2": "while",
        "option3": "do-while",
        "option4": "foreach",
        "answer": "do-while"
    },


    # SQL

    {
        "category": "SQL",
        "question": "Which command retrieves data?",
        "option1": "GET",
        "option2": "SELECT",
        "option3": "FETCH",
        "option4": "READ",
        "answer": "SELECT"
    },

    {
        "category": "SQL",
        "question": "Which command removes a table?",
        "option1": "DELETE",
        "option2": "REMOVE",
        "option3": "DROP",
        "option4": "CLEAR",
        "answer": "DROP"
    },

    {
        "category": "SQL",
        "question": "Which clause filters records?",
        "option1": "WHERE",
        "option2": "FILTER",
        "option3": "HAVING",
        "option4": "WHEN",
        "answer": "WHERE"
    },

    {
        "category": "SQL",
        "question": "Which command adds records?",
        "option1": "ADD",
        "option2": "INSERT",
        "option3": "CREATE",
        "option4": "APPEND",
        "answer": "INSERT"
    },

    {
        "category": "SQL",
        "question": "Which keyword sorts query results?",
        "option1": "SORT BY",
        "option2": "ORDER BY",
        "option3": "GROUP BY",
        "option4": "ARRANGE",
        "answer": "ORDER BY"
    },


    # DBMS

    {
        "category": "DBMS",
        "question": "What does DBMS stand for?",
        "option1": "Database Management System",
        "option2": "Data Backup Management System",
        "option3": "Database Machine System",
        "option4": "Data Management Software",
        "answer": "Database Management System"
    },

    {
        "category": "DBMS",
        "question": "Which key uniquely identifies a record?",
        "option1": "Foreign Key",
        "option2": "Primary Key",
        "option3": "Candidate Key",
        "option4": "Alternate Key",
        "answer": "Primary Key"
    },

    {
        "category": "DBMS",
        "question": "Which normal form removes repeating groups?",
        "option1": "1NF",
        "option2": "2NF",
        "option3": "3NF",
        "option4": "BCNF",
        "answer": "1NF"
    },

    {
        "category": "DBMS",
        "question": "Which key connects tables?",
        "option1": "Primary Key",
        "option2": "Foreign Key",
        "option3": "Super Key",
        "option4": "Unique Key",
        "answer": "Foreign Key"
    },

    {
        "category": "DBMS",
        "question": "What is a collection of related data?",
        "option1": "Database",
        "option2": "Program",
        "option3": "Algorithm",
        "option4": "Network",
        "answer": "Database"
    },


    # DATA STRUCTURES

    {
        "category": "Data Structures",
        "question": "Which data structure follows LIFO?",
        "option1": "Queue",
        "option2": "Stack",
        "option3": "Array",
        "option4": "Tree",
        "answer": "Stack"
    },

    {
        "category": "Data Structures",
        "question": "Which data structure follows FIFO?",
        "option1": "Stack",
        "option2": "Queue",
        "option3": "Tree",
        "option4": "Graph",
        "answer": "Queue"
    },

    {
        "category": "Data Structures",
        "question": "Which structure contains nodes connected by edges?",
        "option1": "Array",
        "option2": "Graph",
        "option3": "Stack",
        "option4": "Queue",
        "answer": "Graph"
    },

    {
        "category": "Data Structures",
        "question": "Which search works on sorted data?",
        "option1": "Linear Search",
        "option2": "Binary Search",
        "option3": "Random Search",
        "option4": "Sequential Search",
        "answer": "Binary Search"
    },

    {
        "category": "Data Structures",
        "question": "What is the top node of a tree called?",
        "option1": "Leaf",
        "option2": "Root",
        "option3": "Child",
        "option4": "Branch",
        "answer": "Root"
    },


    # HTML/CSS

    {
        "category": "HTML/CSS",
        "question": "What does HTML stand for?",
        "option1": "Hyper Text Markup Language",
        "option2": "High Text Machine Language",
        "option3": "Hyperlink Text Management Language",
        "option4": "Home Tool Markup Language",
        "answer": "Hyper Text Markup Language"
    },

    {
        "category": "HTML/CSS",
        "question": "Which tag creates a hyperlink?",
        "option1": "<link>",
        "option2": "<a>",
        "option3": "<href>",
        "option4": "<url>",
        "answer": "<a>"
    },

    {
        "category": "HTML/CSS",
        "question": "What does CSS stand for?",
        "option1": "Computer Style Sheets",
        "option2": "Cascading Style Sheets",
        "option3": "Creative Style System",
        "option4": "Colorful Style Sheets",
        "answer": "Cascading Style Sheets"
    },

    {
        "category": "HTML/CSS",
        "question": "Which CSS property changes text color?",
        "option1": "font-color",
        "option2": "text-color",
        "option3": "color",
        "option4": "foreground",
        "answer": "color"
    },

    {
        "category": "HTML/CSS",
        "question": "Which tag creates the largest heading?",
        "option1": "<h6>",
        "option2": "<heading>",
        "option3": "<h1>",
        "option4": "<head>",
        "answer": "<h1>"
    }
]


# =====================================================
# INITIALIZE DATABASE
# =====================================================

def initialize_database():

    db.create_all()

    if Question.query.count() == 0:

        for item in QUESTION_DATA:

            question = Question(
                category=item["category"],
                question=item["question"],
                option1=item["option1"],
                option2=item["option2"],
                option3=item["option3"],
                option4=item["option4"],
                answer=item["answer"]
            )

            db.session.add(question)

        db.session.commit()

        print("Questions added:", Question.query.count())


with app.app_context():
    initialize_database()


# =====================================================
# HOME
# =====================================================

@app.route("/")
def index():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


# =====================================================
# REGISTER
# =====================================================

@app.route("/register")
def register():

    return render_template("register.html")


@app.route("/api/register", methods=["POST"])
def api_register():

    data = request.get_json()

    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not username or not email or not password:

        return jsonify({
            "success": False,
            "message": "All fields are required"
        })

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:

        return jsonify({
            "success": False,
            "message": "Email already registered"
        })

    user = User(
        username=username,
        email=email,
        password=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Registration successful",
        "redirect": url_for("login")
    })


# =====================================================
# LOGIN
# =====================================================

@app.route("/login")
def login():

    return render_template("login.html")


@app.route("/api/login", methods=["POST"])
def api_login():

    data = request.get_json()

    email = data.get("email", "").strip()
    password = data.get("password", "")

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        })

    if not check_password_hash(
        user.password,
        password
    ):

        return jsonify({
            "success": False,
            "message": "Invalid email or password"
        })

    session["user_id"] = user.id

    return jsonify({
        "success": True,
        "message": "Login successful",
        "redirect": url_for("dashboard")
    })


# =====================================================
# DASHBOARD
# =====================================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = db.session.get(
        User,
        session["user_id"]
    )

    results = Result.query.filter_by(
        user_id=user.id
    ).order_by(
        Result.id.desc()
    ).all()

    quizzes_taken = len(results)

    if results:

        percentages = []

        for result in results:

            if result.total > 0:

                percentages.append(
                    (result.score / result.total) * 100
                )

        average_score = round(
            sum(percentages) / len(percentages)
        )

        best_score = round(
            max(percentages)
        )

    else:

        average_score = 0
        best_score = 0


    # ==========================================
    # GET QUIZ CATEGORIES
    # ==========================================

    categories = db.session.query(
        Question.category
    ).distinct().order_by(
        Question.category
    ).all()

    categories = [
        category[0]
        for category in categories
    ]

    print("AVAILABLE QUIZZES:", categories)


    return render_template(
        "dashboard.html",
        user=user,
        categories=categories,
        quizzes_taken=quizzes_taken,
        average_score=average_score,
        best_score=best_score,
        recent_results=results[:5]
    )


# =====================================================
# QUIZ
# IMPORTANT: <path:category> SUPPORTS HTML/CSS
# =====================================================

@app.route("/quiz/<path:category>")
def quiz(category):

    if "user_id" not in session:

        return redirect(url_for("login"))


    print("QUIZ REQUESTED:", category)


    questions = Question.query.filter_by(
        category=category
    ).all()


    if not questions:

        return f"""
        <h2>No questions found for: {category}</h2>

        <a href="/dashboard">
            Back to Dashboard
        </a>
        """


    random.shuffle(questions)

    questions = questions[:5]


    return render_template(
        "quiz.html",
        questions=questions,
        category=category
    )


# =====================================================
# SUBMIT QUIZ
# =====================================================

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():

    if "user_id" not in session:

        return redirect(url_for("login"))


    category = request.form.get(
        "category"
    )


    questions = Question.query.filter_by(
        category=category
    ).all()


    questions = questions[:5]


    score = 0

    review = []


    for question in questions:

        selected = request.form.get(
            "question_" + str(question.id)
        )


        correct = (
            selected == question.answer
        )


        if correct:
            score += 1


        review.append({
            "question": question.question,
            "selected": selected,
            "answer": question.answer,
            "correct": correct
        })


    total = len(questions)


    result = Result(
        user_id=session["user_id"],
        category=category,
        score=score,
        total=total
    )


    db.session.add(result)

    db.session.commit()


    percentage = 0

    if total > 0:

        percentage = round(
            (score / total) * 100
        )


    return render_template(
        "result.html",
        category=category,
        score=score,
        total=total,
        percentage=percentage,
        review=review
    )


# =====================================================
# HISTORY
# =====================================================

@app.route("/history")
def history():

    if "user_id" not in session:

        return redirect(url_for("login"))


    results = Result.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Result.id.desc()
    ).all()


    return render_template(
        "history.html",
        results=results
    )


# =====================================================
# LOGOUT
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


# =====================================================
# START SERVER
# =====================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )