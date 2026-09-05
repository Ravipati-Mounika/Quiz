from app import app, db, Question
import sqlite3
import os


# ============================================================
# DATABASE LOCATION
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DB_PATH = os.path.join(
    BASE_DIR,
    "quiz.db"
)


# ============================================================
# 100 PROGRAMMING QUESTIONS
# ============================================================

questions = [

    # ========================================================
    # PYTHON - 10 QUESTIONS
    # ========================================================

    (
        "Python",
        "Which keyword is used to define a function in Python?",
        "function",
        "def",
        "define",
        "fun",
        "def"
    ),

    (
        "Python",
        "Which function is used to display output in Python?",
        "echo()",
        "display()",
        "print()",
        "output()",
        "print()"
    ),

    (
        "Python",
        "Which symbol is used for a single-line comment?",
        "//",
        "#",
        "/*",
        "--",
        "#"
    ),

    (
        "Python",
        "Which data type stores True or False?",
        "String",
        "Integer",
        "Boolean",
        "Float",
        "Boolean"
    ),

    (
        "Python",
        "Which collection is ordered and mutable?",
        "Tuple",
        "Set",
        "List",
        "FrozenSet",
        "List"
    ),

    (
        "Python",
        "Which operator is used for exponentiation?",
        "^",
        "**",
        "//",
        "%%",
        "**"
    ),

    (
        "Python",
        "Which function returns the length of a list?",
        "size()",
        "length()",
        "len()",
        "count()",
        "len()"
    ),

    (
        "Python",
        "Which keyword is used to create a class?",
        "object",
        "class",
        "struct",
        "new",
        "class"
    ),

    (
        "Python",
        "Which value represents no value in Python?",
        "null",
        "undefined",
        "None",
        "empty",
        "None"
    ),

    (
        "Python",
        "Which file extension is used for Python programs?",
        ".python",
        ".pt",
        ".py",
        ".p",
        ".py"
    ),


    # ========================================================
    # JAVA - 10 QUESTIONS
    # ========================================================

    (
        "Java",
        "Which keyword is used to define a class in Java?",
        "class",
        "struct",
        "define",
        "object",
        "class"
    ),

    (
        "Java",
        "Which method is the entry point of a Java application?",
        "start()",
        "main()",
        "run()",
        "execute()",
        "main()"
    ),

    (
        "Java",
        "Which keyword creates an object?",
        "create",
        "object",
        "new",
        "make",
        "new"
    ),

    (
        "Java",
        "Which data type stores whole numbers?",
        "float",
        "String",
        "int",
        "boolean",
        "int"
    ),

    (
        "Java",
        "Which keyword is used for inheritance?",
        "inherits",
        "extends",
        "implements",
        "super",
        "extends"
    ),

    (
        "Java",
        "Which keyword is used when a class implements an interface?",
        "extends",
        "inherits",
        "implements",
        "interface",
        "implements"
    ),

    (
        "Java",
        "Which keyword prevents a variable from being changed?",
        "constant",
        "final",
        "static",
        "fixed",
        "final"
    ),

    (
        "Java",
        "Which type is used to store text?",
        "Text",
        "String",
        "char[]",
        "text",
        "String"
    ),

    (
        "Java",
        "Which symbol ends most Java statements?",
        ".",
        ":",
        ";",
        ",",
        ";"
    ),

    (
        "Java",
        "Java source files normally use which extension?",
        ".java",
        ".jav",
        ".class",
        ".j",
        ".java"
    ),


    # ========================================================
    # C - 10 QUESTIONS
    # ========================================================

    (
        "C",
        "Which function is commonly used to print output in C?",
        "print()",
        "printf()",
        "display()",
        "cout",
        "printf()"
    ),

    (
        "C",
        "Which function is used to read formatted input?",
        "input()",
        "scanf()",
        "read()",
        "cin",
        "scanf()"
    ),

    (
        "C",
        "Which header file is required for printf()?",
        "<stdlib.h>",
        "<stdio.h>",
        "<string.h>",
        "<math.h>",
        "<stdio.h>"
    ),

    (
        "C",
        "Which symbol is used to end a C statement?",
        ":",
        ".",
        ";",
        ",",
        ";"
    ),

    (
        "C",
        "Which data type stores a single character?",
        "string",
        "char",
        "character",
        "text",
        "char"
    ),

    (
        "C",
        "Which operator is used to get the address of a variable?",
        "*",
        "&",
        "#",
        "@",
        "&"
    ),

    (
        "C",
        "Which operator is used to dereference a pointer?",
        "&",
        "*",
        "#",
        "%",
        "*"
    ),

    (
        "C",
        "Which keyword is used to define a constant variable?",
        "constant",
        "const",
        "fixed",
        "final",
        "const"
    ),

    (
        "C",
        "Which loop executes while a condition is true?",
        "repeat",
        "while",
        "loop",
        "foreach",
        "while"
    ),

    (
        "C",
        "Which extension is commonly used for C source files?",
        ".cpp",
        ".c",
        ".h",
        ".cc",
        ".c"
    ),


    # ========================================================
    # C++ - 10 QUESTIONS
    # ========================================================

    (
        "C++",
        "Which object is commonly used for output in C++?",
        "printf",
        "cout",
        "output",
        "print",
        "cout"
    ),

    (
        "C++",
        "Which object is commonly used for input in C++?",
        "scanf",
        "cin",
        "input",
        "read",
        "cin"
    ),

    (
        "C++",
        "Which header provides cout and cin?",
        "<stdio.h>",
        "<iostream>",
        "<string.h>",
        "<input.h>",
        "<iostream>"
    ),

    (
        "C++",
        "Which keyword is used to create a class?",
        "object",
        "class",
        "struct",
        "define",
        "class"
    ),

    (
        "C++",
        "Which feature allows the same function name with different parameters?",
        "Inheritance",
        "Encapsulation",
        "Function overloading",
        "Abstraction",
        "Function overloading"
    ),

    (
        "C++",
        "Which operator is used with cout?",
        ">>",
        "<<",
        "=>",
        "::",
        "<<"
    ),

    (
        "C++",
        "Which operator is used with cin?",
        "<<",
        ">>",
        "::",
        "==",
        ">>"
    ),

    (
        "C++",
        "Which keyword is used for inheritance?",
        "extends",
        "inherits",
        ":",
        "implements",
        ":"
    ),

    (
        "C++",
        "Which extension is commonly used for C++ source files?",
        ".c",
        ".java",
        ".cpp",
        ".py",
        ".cpp"
    ),

    (
        "C++",
        "Which feature allows a class to have multiple constructors?",
        "Constructor overloading",
        "Inheritance",
        "Pointers",
        "Templates",
        "Constructor overloading"
    ),


    # ========================================================
    # JAVASCRIPT - 10 QUESTIONS
    # ========================================================

    (
        "JavaScript",
        "Which keyword declares a block-scoped variable that can be reassigned?",
        "const",
        "let",
        "fixed",
        "define",
        "let"
    ),

    (
        "JavaScript",
        "Which keyword declares a constant?",
        "var",
        "let",
        "const",
        "constant",
        "const"
    ),

    (
        "JavaScript",
        "Which function prints a message to the browser console?",
        "print()",
        "console.log()",
        "console.print()",
        "log()",
        "console.log()"
    ),

    (
        "JavaScript",
        "Which operator checks strict equality?",
        "=",
        "==",
        "===",
        "!=",
        "==="
    ),

    (
        "JavaScript",
        "Which method adds an element to the end of an array?",
        "add()",
        "append()",
        "push()",
        "insert()",
        "push()"
    ),

    (
        "JavaScript",
        "Which method removes the last element from an array?",
        "remove()",
        "pop()",
        "delete()",
        "last()",
        "pop()"
    ),

    (
        "JavaScript",
        "Which keyword is used to define a function?",
        "def",
        "function",
        "func",
        "method",
        "function"
    ),

    (
        "JavaScript",
        "Which object represents the current web page?",
        "browser",
        "document",
        "page",
        "html",
        "document"
    ),

    (
        "JavaScript",
        "Which method converts JSON text into an object?",
        "JSON.convert()",
        "JSON.parse()",
        "JSON.object()",
        "JSON.read()",
        "JSON.parse()"
    ),

    (
        "JavaScript",
        "Which symbol starts a single-line comment?",
        "#",
        "//",
        "<!--",
        "/*",
        "//"
    ),


    # ========================================================
    # REACT JS - 10 QUESTIONS
    # ========================================================

    (
        "React JS",
        "Who originally developed React?",
        "Google",
        "Facebook",
        "Microsoft",
        "Apple",
        "Facebook"
    ),

    (
        "React JS",
        "What is React primarily used for?",
        "Database management",
        "Building user interfaces",
        "Operating systems",
        "File compression",
        "Building user interfaces"
    ),

    (
        "React JS",
        "Which syntax is commonly used to write HTML-like elements in React?",
        "XML",
        "JSX",
        "JQuery",
        "TSXOnly",
        "JSX"
    ),

    (
        "React JS",
        "Which hook is used to manage state in a functional component?",
        "useEffect",
        "useState",
        "useData",
        "useValue",
        "useState"
    ),

    (
        "React JS",
        "Which hook is commonly used for side effects?",
        "useState",
        "useEffect",
        "useSideEffect",
        "useAction",
        "useEffect"
    ),

    (
        "React JS",
        "What does JSX stand for?",
        "JavaScript XML",
        "Java Syntax Extension",
        "JavaScript Extension",
        "JSON XML",
        "JavaScript XML"
    ),

    (
        "React JS",
        "What is used to pass data from a parent component to a child?",
        "State",
        "Props",
        "Hooks",
        "Events",
        "Props"
    ),

    (
        "React JS",
        "Which command commonly creates a React project using Vite?",
        "npm create vite@latest",
        "npm install react-project",
        "react new",
        "create-react",
        "npm create vite@latest"
    ),

    (
        "React JS",
        "What should be used for a unique key when rendering a list?",
        "A unique identifier",
        "The array color",
        "The component name",
        "The CSS class",
        "A unique identifier"
    ),

    (
        "React JS",
        "React components are commonly written as what?",
        "Functions",
        "Database tables",
        "SQL queries",
        "CSS files",
        "Functions"
    ),


    # ========================================================
    # HTML - 10 QUESTIONS
    # ========================================================

    (
        "HTML",
        "What does HTML stand for?",
        "Hyper Text Markup Language",
        "High Text Machine Language",
        "Hyperlink Text Management Language",
        "Home Tool Markup Language",
        "Hyper Text Markup Language"
    ),

    (
        "HTML",
        "Which tag creates the largest heading?",
        "<h6>",
        "<head>",
        "<h1>",
        "<heading>",
        "<h1>"
    ),

    (
        "HTML",
        "Which tag creates a paragraph?",
        "<para>",
        "<text>",
        "<p>",
        "<paragraph>",
        "<p>"
    ),

    (
        "HTML",
        "Which tag creates a hyperlink?",
        "<link>",
        "<a>",
        "<href>",
        "<url>",
        "<a>"
    ),

    (
        "HTML",
        "Which tag displays an image?",
        "<image>",
        "<img>",
        "<picture>",
        "<src>",
        "<img>"
    ),

    (
        "HTML",
        "Which attribute specifies the image source?",
        "href",
        "src",
        "link",
        "url",
        "src"
    ),

    (
        "HTML",
        "Which tag creates an unordered list?",
        "<ol>",
        "<ul>",
        "<list>",
        "<li>",
        "<ul>"
    ),

    (
        "HTML",
        "Which tag creates a line break?",
        "<break>",
        "<lb>",
        "<br>",
        "<newline>",
        "<br>"
    ),

    (
        "HTML",
        "Which tag creates a button?",
        "<btn>",
        "<button>",
        "<click>",
        "<inputbutton>",
        "<button>"
    ),

    (
        "HTML",
        "Which attribute provides alternative text for an image?",
        "title",
        "alt",
        "text",
        "description",
        "alt"
    ),


    # ========================================================
    # CSS - 10 QUESTIONS
    # ========================================================

    (
        "CSS",
        "What does CSS stand for?",
        "Computer Style Sheets",
        "Cascading Style Sheets",
        "Creative Style System",
        "Colorful Style Sheets",
        "Cascading Style Sheets"
    ),

    (
        "CSS",
        "Which property changes text color?",
        "font-color",
        "text-color",
        "color",
        "foreground",
        "color"
    ),

    (
        "CSS",
        "Which property changes the background color?",
        "background-color",
        "bg-color",
        "background",
        "color-background",
        "background-color"
    ),

    (
        "CSS",
        "Which property changes font size?",
        "text-size",
        "font-size",
        "size",
        "font",
        "font-size"
    ),

    (
        "CSS",
        "Which property makes text bold?",
        "font-weight",
        "text-bold",
        "bold",
        "font-style",
        "font-weight"
    ),

    (
        "CSS",
        "Which symbol selects an element by ID?",
        ".",
        "#",
        "*",
        "@",
        "#"
    ),

    (
        "CSS",
        "Which symbol selects an element by class?",
        "#",
        ".",
        "@",
        "&",
        "."
    ),

    (
        "CSS",
        "Which property controls space inside an element?",
        "margin",
        "padding",
        "border",
        "spacing",
        "padding"
    ),

    (
        "CSS",
        "Which property controls space outside an element?",
        "padding",
        "margin",
        "border",
        "outside",
        "margin"
    ),

    (
        "CSS",
        "Which layout system is commonly used for flexible one-dimensional layouts?",
        "Float",
        "Flexbox",
        "Table",
        "Inline",
        "Flexbox"
    ),


    # ========================================================
    # SQL - 10 QUESTIONS
    # ========================================================

    (
        "SQL",
        "What does SQL stand for?",
        "Structured Query Language",
        "Simple Query Language",
        "System Query Language",
        "Structured Question Language",
        "Structured Query Language"
    ),

    (
        "SQL",
        "Which command is used to retrieve data?",
        "GET",
        "SELECT",
        "FETCHDATA",
        "READ",
        "SELECT"
    ),

    (
        "SQL",
        "Which command is used to add new records?",
        "ADD",
        "INSERT",
        "CREATE",
        "PUT",
        "INSERT"
    ),

    (
        "SQL",
        "Which command is used to modify existing records?",
        "CHANGE",
        "MODIFY",
        "UPDATE",
        "EDIT",
        "UPDATE"
    ),

    (
        "SQL",
        "Which command removes records from a table?",
        "REMOVE",
        "DELETE",
        "DROP ROW",
        "CLEAR",
        "DELETE"
    ),

    (
        "SQL",
        "Which clause filters rows?",
        "FILTER",
        "WHERE",
        "HAVINGONLY",
        "SEARCH",
        "WHERE"
    ),

    (
        "SQL",
        "Which clause sorts query results?",
        "SORT BY",
        "ORDER BY",
        "GROUP BY",
        "SORT",
        "ORDER BY"
    ),

    (
        "SQL",
        "Which keyword removes duplicate results?",
        "UNIQUE",
        "DISTINCT",
        "ONLY",
        "DIFFERENT",
        "DISTINCT"
    ),

    (
        "SQL",
        "Which function counts rows?",
        "TOTAL()",
        "COUNT()",
        "ROWS()",
        "NUMBER()",
        "COUNT()"
    ),

    (
        "SQL",
        "Which command creates a new table?",
        "NEW TABLE",
        "CREATE TABLE",
        "MAKE TABLE",
        "ADD TABLE",
        "CREATE TABLE"
    ),


    # ========================================================
    # FLASK - 10 QUESTIONS
    # ========================================================

    (
        "Flask",
        "What is Flask?",
        "A Python web framework",
        "A database",
        "A JavaScript library",
        "An operating system",
        "A Python web framework"
    ),

    (
        "Flask",
        "Which Python package provides Flask?",
        "flask",
        "django",
        "requests",
        "numpy",
        "flask"
    ),

    (
        "Flask",
        "Which decorator defines a URL route?",
        "@app.route",
        "@app.url",
        "@route.url",
        "@flask.path",
        "@app.route"
    ),

    (
        "Flask",
        "Which function renders an HTML template?",
        "show_template()",
        "render_template()",
        "html()",
        "template()",
        "render_template()"
    ),

    (
        "Flask",
        "Which object is used to access incoming request data?",
        "request",
        "input",
        "incoming",
        "data",
        "request"
    ),

    (
        "Flask",
        "Which function returns JSON responses?",
        "return_json()",
        "jsonify()",
        "json_response()",
        "make_json()",
        "jsonify()"
    ),

    (
        "Flask",
        "Which object is commonly used to store user session data?",
        "session",
        "cookie_data",
        "storage",
        "user_data",
        "session"
    ),

    (
        "Flask",
        "Which HTTP method is commonly used to submit form data?",
        "GET",
        "POST",
        "SEND",
        "PUTFORM",
        "POST"
    ),

    (
        "Flask",
        "Which file is commonly used to start a Flask application?",
        "app.py",
        "flask.html",
        "server.css",
        "main.sql",
        "app.py"
    ),

    (
        "Flask",
        "Which command commonly starts a Flask development server?",
        "python app.py",
        "run flask now",
        "start flask",
        "flask start server only",
        "python app.py"
    )
]


# ============================================================
# VERIFY QUESTION COUNT
# ============================================================

if len(questions) != 100:

    print(
        f"ERROR: Expected 100 questions, "
        f"but found {len(questions)}."
    )

    raise SystemExit(1)


# ============================================================
# CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect(
    DB_PATH
)

cursor = connection.cursor()


# ============================================================
# CREATE QUESTIONS TABLE
# ============================================================

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer TEXT NOT NULL
    )
    """
)


# ============================================================
# REMOVE OLD QUESTIONS
# ============================================================

cursor.execute(
    "DELETE FROM questions"
)


# ============================================================
# RESET AUTOINCREMENT
# ============================================================

try:

    cursor.execute(
        "DELETE FROM sqlite_sequence "
        "WHERE name = 'questions'"
    )

except sqlite3.OperationalError:

    pass


# ============================================================
# INSERT 100 QUESTIONS
# ============================================================

cursor.executemany(
    """
    INSERT INTO questions (
        category,
        question,
        option1,
        option2,
        option3,
        option4,
        answer
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    questions
)


# ============================================================
# SAVE DATABASE
# ============================================================

connection.commit()


# ============================================================
# DISPLAY RESULTS
# ============================================================

print()
print("=" * 60)
print("       QUIZMASTER QUESTION DATABASE")
print("=" * 60)

print()

print(
    f"Successfully added {len(questions)} questions."
)

print()

print("Questions by category:")
print("-" * 60)


cursor.execute(
    """
    SELECT category, COUNT(*)
    FROM questions
    GROUP BY category
    ORDER BY category
    """
)

categories = cursor.fetchall()


for category, count in categories:

    print(
        f"{category:<20} {count} questions"
    )


print("-" * 60)


cursor.execute(
    "SELECT COUNT(*) FROM questions"
)

total = cursor.fetchone()[0]


print(
    f"{'TOTAL':<20} {total} questions"
)

print()

print("Database:")
print(DB_PATH)

print()

print("Done!")

print("=" * 60)


# ============================================================
# CLOSE DATABASE
# ============================================================

cursor.close()

connection.close()
