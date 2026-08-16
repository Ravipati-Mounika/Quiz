from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = "quiz_application_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =========================================================
# DATABASE MODELS
# =========================================================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    question = db.Column(db.String(500), nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    option4 = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)


# =========================================================
# HOME
# =========================================================

@app.route("/")
def index():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


# =========================================================
# REGISTER
# =========================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not username or not email or not password:
            flash("Please fill all fields.")
            return redirect(url_for("register"))

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            flash("Email already registered.")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.")

        return redirect(url_for("login"))

    return render_template("register.html")


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

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

            return redirect(url_for("dashboard"))

        flash("Invalid email or password.")

    return render_template("login.html")


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    results = Result.query.filter_by(
        username=user.username
    ).order_by(
        Result.id.desc()
    ).all()

    category_rows = db.session.query(
        Question.category
    ).distinct().all()

    categories = [
        row[0]
        for row in category_rows
    ]

    total_quizzes = len(results)

    if results:

        average_score = round(
            sum(
                (r.score / r.total) * 100
                for r in results
            ) / len(results)
        )

        best_score = max(
            round(
                (r.score / r.total) * 100
            )
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


# =========================================================
# QUIZ
# =========================================================

@app.route("/quiz/<category>")
def quiz(category):

    if "user_id" not in session:
        return redirect(url_for("login"))

    questions = Question.query.filter_by(
        category=category
    ).all()

    if not questions:

        flash("No questions available for this category.")

        return redirect(url_for("dashboard"))

    random.shuffle(questions)

    questions = questions[:10]

    session["quiz_question_ids"] = [
        q.id for q in questions
    ]

    session["quiz_category"] = category

    return render_template(
        "quiz.html",
        questions=questions,
        category=category
    )


# =========================================================
# SUBMIT QUIZ
# =========================================================

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():

    if "user_id" not in session:
        return redirect(url_for("login"))

    question_ids = session.get(
        "quiz_question_ids",
        []
    )

    category = session.get(
        "quiz_category",
        "General"
    )

    if not question_ids:

        flash("Quiz session expired.")

        return redirect(url_for("dashboard"))

    score = 0
    review = []

    for question_id in question_ids:

        question = Question.query.get(question_id)

        if not question:
            continue

        selected = request.form.get(
            f"question_{question.id}"
        )

        is_correct = (
            selected == question.answer
        )

        if is_correct:
            score += 1

        review.append({
            "question": question.question,
            "selected": selected,
            "correct_answer": question.answer,
            "correct": is_correct
        })

    total = len(question_ids)

    result = Result(
        username=session["username"],
        category=category,
        score=score,
        total=total
    )

    db.session.add(result)
    db.session.commit()

    session["review"] = review

    session.pop("quiz_question_ids", None)
    session.pop("quiz_category", None)

    return redirect(
        url_for(
            "result",
            score=score,
            total=total
        )
    )


# =========================================================
# RESULT
# =========================================================

@app.route("/result/<int:score>/<int:total>")
def result(score, total):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if total > 0:
        percentage = round(
            (score / total) * 100
        )
    else:
        percentage = 0

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


# =========================================================
# HISTORY
# =========================================================

@app.route("/history")
def history():

    if "user_id" not in session:
        return redirect(url_for("login"))

    results = Result.query.filter_by(
        username=session["username"]
    ).order_by(
        Result.id.desc()
    ).all()

    return render_template(
        "history.html",
        results=results
    )


# =========================================================
# ADMIN
# =========================================================

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        question = Question(
            category=request.form.get("category"),
            question=request.form.get("question"),
            option1=request.form.get("option1"),
            option2=request.form.get("option2"),
            option3=request.form.get("option3"),
            option4=request.form.get("option4"),
            answer=request.form.get("answer")
        )

        db.session.add(question)
        db.session.commit()

        flash("Question added successfully.")

        return redirect(url_for("admin"))

    questions = Question.query.order_by(
        Question.category
    ).all()

    return render_template(
        "admin.html",
        questions=questions
    )


# =========================================================
# INITIAL QUESTIONS
# =========================================================

def create_questions():

    if Question.query.count() > 0:
        return

    questions = [

        # ---------------- PYTHON ----------------

        Question(
            category="Python",
            question="Which keyword is used to define a function?",
            option1="function",
            option2="def",
            option3="define",
            option4="fun",
            answer="def"
        ),

        Question(
            category="Python",
            question="Which function displays output?",
            option1="show()",
            option2="display()",
            option3="print()",
            option4="output()",
            answer="print()"
        ),

        Question(
            category="Python",
            question="Which collection stores unique values?",
            option1="List",
            option2="Tuple",
            option3="Set",
            option4="String",
            answer="Set"
        ),

        Question(
            category="Python",
            question="Which function returns length?",
            option1="size()",
            option2="length()",
            option3="len()",
            option4="count()",
            answer="len()"
        ),

        Question(
            category="Python",
            question="What is the extension of Python files?",
            option1=".java",
            option2=".py",
            option3=".python",
            option4=".pt",
            answer=".py"
        ),

        Question(
            category="Python",
            question="Which keyword creates a class?",
            option1="class",
            option2="Class",
            option3="struct",
            option4="object",
            answer="class"
        ),

        Question(
            category="Python",
            question="Which value represents no value?",
            option1="null",
            option2="nil",
            option3="None",
            option4="void",
            answer="None"
        ),

        Question(
            category="Python",
            question="Which symbol starts a comment?",
            option1="//",
            option2="#",
            option3="/*",
            option4="--",
            answer="#"
        ),

        Question(
            category="Python",
            question="Which loop iterates over a sequence?",
            option1="repeat",
            option2="for",
            option3="loop",
            option4="iterate",
            answer="for"
        ),

        Question(
            category="Python",
            question="Which data type stores True or False?",
            option1="int",
            option2="str",
            option3="bool",
            option4="float",
            answer="bool"
        ),

        # ---------------- JAVA ----------------

        Question(
            category="Java",
            question="Which keyword creates an object?",
            option1="create",
            option2="object",
            option3="new",
            option4="make",
            answer="new"
        ),

        Question(
            category="Java",
            question="Which method is the entry point?",
            option1="start()",
            option2="main()",
            option3="run()",
            option4="execute()",
            answer="main()"
        ),

        Question(
            category="Java",
            question="Which keyword is used for inheritance?",
            option1="inherit",
            option2="extends",
            option3="inherits",
            option4="parent",
            answer="extends"
        ),

        Question(
            category="Java",
            question="Which type stores true or false?",
            option1="int",
            option2="boolean",
            option3="char",
            option4="String",
            answer="boolean"
        ),

        Question(
            category="Java",
            question="Which keyword refers to the current object?",
            option1="self",
            option2="this",
            option3="current",
            option4="object",
            answer="this"
        ),

        Question(
            category="Java",
            question="Which package contains Scanner?",
            option1="java.io",
            option2="java.util",
            option3="java.sql",
            option4="java.lang",
            answer="java.util"
        ),

        Question(
            category="Java",
            question="Which keyword prevents inheritance?",
            option1="static",
            option2="final",
            option3="private",
            option4="stop",
            answer="final"
        ),

        Question(
            category="Java",
            question="Which concept means many forms?",
            option1="Inheritance",
            option2="Polymorphism",
            option3="Encapsulation",
            option4="Compilation",
            answer="Polymorphism"
        ),

        Question(
            category="Java",
            question="Which keyword handles exceptions?",
            option1="try",
            option2="error",
            option3="handle",
            option4="catching",
            answer="try"
        ),

        Question(
            category="Java",
            question="Which keyword is used to implement an interface?",
            option1="extends",
            option2="implements",
            option3="interface",
            option4="inherit",
            answer="implements"
        ),

        # ---------------- C ----------------

        Question(
            category="C",
            question="Who developed C?",
            option1="James Gosling",
            option2="Dennis Ritchie",
            option3="Guido van Rossum",
            option4="Bjarne Stroustrup",
            answer="Dennis Ritchie"
        ),

        Question(
            category="C",
            question="Which function starts a C program?",
            option1="start()",
            option2="main()",
            option3="run()",
            option4="begin()",
            answer="main()"
        ),

        Question(
            category="C",
            question="Which symbol terminates a statement?",
            option1=":",
            option2=".",
            option3=";",
            option4=",",
            answer=";"
        ),

        Question(
            category="C",
            question="Which header contains printf()?",
            option1="stdlib.h",
            option2="stdio.h",
            option3="string.h",
            option4="math.h",
            answer="stdio.h"
        ),

        Question(
            category="C",
            question="Which operator gets an address?",
            option1="*",
            option2="&",
            option3="#",
            option4="%",
            answer="&"
        ),

        Question(
            category="C",
            question="Which type stores a character?",
            option1="char",
            option2="string",
            option3="text",
            option4="character",
            answer="char"
        ),

        Question(
            category="C",
            question="Which loop executes at least once?",
            option1="for",
            option2="while",
            option3="do-while",
            option4="foreach",
            answer="do-while"
        ),

        Question(
            category="C",
            question="Which keyword returns a value?",
            option1="send",
            option2="return",
            option3="result",
            option4="output",
            answer="return"
        ),

        Question(
            category="C",
            question="Which symbol declares a pointer?",
            option1="&",
            option2="*",
            option3="#",
            option4="@",
            answer="*"
        ),

        Question(
            category="C",
            question="Which header handles strings?",
            option1="stdio.h",
            option2="string.h",
            option3="math.h",
            option4="stdlib.h",
            answer="string.h"
        ),

        # ---------------- SQL ----------------

        Question(
            category="SQL",
            question="Which command retrieves data?",
            option1="INSERT",
            option2="SELECT",
            option3="UPDATE",
            option4="DELETE",
            answer="SELECT"
        ),

        Question(
            category="SQL",
            question="Which command adds records?",
            option1="ADD",
            option2="INSERT",
            option3="CREATE",
            option4="PUT",
            answer="INSERT"
        ),

        Question(
            category="SQL",
            question="Which command modifies records?",
            option1="CHANGE",
            option2="UPDATE",
            option3="MODIFY",
            option4="ALTER",
            answer="UPDATE"
        ),

        Question(
            category="SQL",
            question="Which command removes rows?",
            option1="REMOVE",
            option2="DELETE",
            option3="DROP",
            option4="CLEAR",
            answer="DELETE"
        ),

        Question(
            category="SQL",
            question="Which key uniquely identifies a record?",
            option1="Foreign Key",
            option2="Primary Key",
            option3="Secondary Key",
            option4="Candidate Key",
            answer="Primary Key"
        ),

        Question(
            category="SQL",
            question="Which clause filters records?",
            option1="ORDER BY",
            option2="WHERE",
            option3="GROUP BY",
            option4="SORT",
            answer="WHERE"
        ),

        Question(
            category="SQL",
            question="Which function counts rows?",
            option1="SUM()",
            option2="COUNT()",
            option3="TOTAL()",
            option4="NUMBER()",
            answer="COUNT()"
        ),

        Question(
            category="SQL",
            question="Which command deletes a table?",
            option1="DELETE",
            option2="DROP",
            option3="REMOVE",
            option4="CLEAR",
            answer="DROP"
        ),

        Question(
            category="SQL",
            question="Which clause sorts records?",
            option1="SORT BY",
            option2="ORDER BY",
            option3="GROUP BY",
            option4="ARRANGE BY",
            answer="ORDER BY"
        ),

        Question(
            category="SQL",
            question="Which keyword removes duplicates?",
            option1="UNIQUE",
            option2="DISTINCT",
            option3="DIFFERENT",
            option4="FILTER",
            answer="DISTINCT"
        ),

        # ---------------- DATA STRUCTURES ----------------

        Question(
            category="Data Structures",
            question="Which data structure follows LIFO?",
            option1="Queue",
            option2="Stack",
            option3="Tree",
            option4="Graph",
            answer="Stack"
        ),

        Question(
            category="Data Structures",
            question="Which data structure follows FIFO?",
            option1="Stack",
            option2="Queue",
            option3="Tree",
            option4="Array",
            answer="Queue"
        ),

        Question(
            category="Data Structures",
            question="Which search requires sorted data?",
            option1="Linear Search",
            option2="Binary Search",
            option3="Random Search",
            option4="Sequential Search",
            answer="Binary Search"
        ),

        Question(
            category="Data Structures",
            question="Which structure contains nodes and edges?",
            option1="Array",
            option2="Stack",
            option3="Graph",
            option4="Queue",
            answer="Graph"
        ),

        Question(
            category="Data Structures",
            question="Which structure has a root node?",
            option1="Tree",
            option2="Array",
            option3="Queue",
            option4="Stack",
            answer="Tree"
        ),

        Question(
            category="Data Structures",
            question="Which structure uses linked nodes?",
            option1="Array",
            option2="Linked List",
            option3="Matrix",
            option4="String",
            answer="Linked List"
        ),

        Question(
            category="Data Structures",
            question="What is the top element of a stack called?",
            option1="Front",
            option2="Rear",
            option3="Top",
            option4="Root",
            answer="Top"
        ),

        Question(
            category="Data Structures",
            question="Which algorithm finds shortest paths?",
            option1="Dijkstra's Algorithm",
            option2="Bubble Sort",
            option3="Merge Sort",
            option4="Binary Search",
            answer="Dijkstra's Algorithm"
        ),

        Question(
            category="Data Structures",
            question="Which sorting algorithm uses divide and conquer?",
            option1="Bubble Sort",
            option2="Merge Sort",
            option3="Selection Sort",
            option4="Linear Sort",
            answer="Merge Sort"
        ),

        Question(
            category="Data Structures",
            question="Which structure is used in BFS?",
            option1="Stack",
            option2="Queue",
            option3="Heap",
            option4="Tree",
            answer="Queue"
        ),

        # ---------------- DBMS ----------------

        Question(
            category="DBMS",
            question="What does DBMS stand for?",
            option1="Database Management System",
            option2="Data Backup Management System",
            option3="Database Machine System",
            option4="Data Management Software",
            answer="Database Management System"
        ),

        Question(
            category="DBMS",
            question="Which key connects two tables?",
            option1="Primary Key",
            option2="Foreign Key",
            option3="Super Key",
            option4="Unique Key",
            answer="Foreign Key"
        ),

        Question(
            category="DBMS",
            question="Which normal form removes repeating groups?",
            option1="1NF",
            option2="2NF",
            option3="3NF",
            option4="BCNF",
            answer="1NF"
        ),

        Question(
            category="DBMS",
            question="Which model stores data in tables?",
            option1="Network",
            option2="Relational",
            option3="Object",
            option4="Hierarchical",
            answer="Relational"
        ),

        Question(
            category="DBMS",
            question="Which command is DDL?",
            option1="SELECT",
            option2="INSERT",
            option3="CREATE",
            option4="UPDATE",
            answer="CREATE"
        ),

        Question(
            category="DBMS",
            question="Which property means all-or-nothing?",
            option1="Consistency",
            option2="Atomicity",
            option3="Isolation",
            option4="Durability",
            answer="Atomicity"
        ),

        Question(
            category="DBMS",
            question="Which command removes a table?",
            option1="DELETE",
            option2="DROP",
            option3="REMOVE",
            option4="CLEAR",
            answer="DROP"
        ),

        Question(
            category="DBMS",
            question="What is a collection of related data?",
            option1="Database",
            option2="Program",
            option3="Algorithm",
            option4="Compiler",
            answer="Database"
        ),

        # ---------------- HTML/CSS ----------------

        Question(
            category="HTML/CSS",
            question="What does HTML stand for?",
            option1="Hyper Text Markup Language",
            option2="High Text Machine Language",
            option3="Hyperlink Text Management Language",
            option4="Home Tool Markup Language",
            answer="Hyper Text Markup Language"
        ),

        Question(
            category="HTML/CSS",
            question="Which tag creates a hyperlink?",
            option1="<link>",
            option2="<a>",
            option3="<href>",
            option4="<url>",
            answer="<a>"
        ),

        Question(
            category="HTML/CSS",
            question="Which tag creates a paragraph?",
            option1="<para>",
            option2="<p>",
            option3="<paragraph>",
            option4="<text>",
            answer="<p>"
        ),

        Question(
            category="HTML/CSS",
            question="Which language styles web pages?",
            option1="HTML",
            option2="CSS",
            option3="SQL",
            option4="Python",
            answer="CSS"
        ),

        Question(
            category="HTML/CSS",
            question="Which CSS property changes text color?",
            option1="font",
            option2="text-color",
            option3="color",
            option4="foreground",
            answer="color"
        ),

        Question(
            category="HTML/CSS",
            question="Which tag displays an image?",
            option1="<image>",
            option2="<img>",
            option3="<picture>",
            option4="<src>",
            answer="<img>"
        ),

        Question(
            category="HTML/CSS",
            question="Which is the largest HTML heading?",
            option1="<h6>",
            option2="<heading>",
            option3="<h1>",
            option4="<head>",
            answer="<h1>"
        ),

        Question(
            category="HTML/CSS",
            question="Which CSS property changes background color?",
            option1="background-color",
            option2="bgcolor",
            option3="background",
            option4="color-background",
            answer="background-color"
        )
    ]

    db.session.add_all(questions)
    db.session.commit()

    print(
        f"Added {len(questions)} questions."
    )


# =========================================================
# CREATE DATABASE
# =========================================================

with app.app_context():

    db.create_all()

    create_questions()


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )