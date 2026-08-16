from app import app, db, Question


questions = [

# =====================
# PYTHON
# =====================

Question(
    category="Python",
    question="Which keyword is used to create a function?",
    option1="function",
    option2="def",
    option3="fun",
    option4="define",
    answer="def"
),

Question(
    category="Python",
    question="Which function prints output?",
    option1="print()",
    option2="output()",
    option3="display()",
    option4="show()",
    answer="print()"
),

Question(
    category="Python",
    question="Which data type stores multiple values?",
    option1="int",
    option2="float",
    option3="list",
    option4="bool",
    answer="list"
),

Question(
    category="Python",
    question="Which keyword is used for a loop?",
    option1="repeat",
    option2="for",
    option3="loop",
    option4="iterate",
    answer="for"
),

Question(
    category="Python",
    question="Which symbol is used for comments?",
    option1="//",
    option2="#",
    option3="/*",
    option4="--",
    answer="#"
),

Question(
    category="Python",
    question="What is the output type of input()?",
    option1="Integer",
    option2="Float",
    option3="String",
    option4="Boolean",
    answer="String"
),

Question(
    category="Python",
    question="Which keyword creates a class?",
    option1="class",
    option2="Class",
    option3="object",
    option4="struct",
    answer="class"
),

Question(
    category="Python",
    question="Which collection does not allow duplicate values?",
    option1="List",
    option2="Tuple",
    option3="Set",
    option4="String",
    answer="Set"
),

Question(
    category="Python",
    question="Which function returns the length?",
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


# =====================
# JAVA
# =====================

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
    option3="implements",
    option4="super",
    answer="extends"
),

Question(
    category="Java",
    question="Which keyword prevents inheritance?",
    option1="static",
    option2="private",
    option3="final",
    option4="constant",
    answer="final"
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
    question="Which concept means hiding implementation details?",
    option1="Inheritance",
    option2="Polymorphism",
    option3="Abstraction",
    option4="Compilation",
    answer="Abstraction"
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
    option3="java.lang",
    option4="java.sql",
    answer="java.util"
),

Question(
    category="Java",
    question="Which concept allows method overloading?",
    option1="Polymorphism",
    option2="Inheritance",
    option3="Abstraction",
    option4="Encapsulation",
    answer="Polymorphism"
),

Question(
    category="Java",
    question="Which keyword handles exceptions?",
    option1="try",
    option2="test",
    option3="error",
    option4="check",
    answer="try"
),


# =====================
# SQL
# =====================

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
    question="Which command adds a new row?",
    option1="ADD",
    option2="INSERT",
    option3="CREATE",
    option4="PUT",
    answer="INSERT"
),

Question(
    category="SQL",
    question="Which command modifies existing data?",
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
    question="Which key uniquely identifies a row?",
    option1="Foreign Key",
    option2="Primary Key",
    option3="Secondary Key",
    option4="Candidate Key",
    answer="Primary Key"
),

Question(
    category="SQL",
    question="Which clause filters rows?",
    option1="WHERE",
    option2="FILTER",
    option3="HAVING",
    option4="CHECK",
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
    question="Which command removes a table?",
    option1="DELETE",
    option2="REMOVE",
    option3="DROP",
    option4="CLEAR",
    answer="DROP"
),

Question(
    category="SQL",
    question="Which clause sorts data?",
    option1="SORT BY",
    option2="ORDER BY",
    option3="GROUP BY",
    option4="ARRANGE BY",
    answer="ORDER BY"
),

Question(
    category="SQL",
    question="Which keyword removes duplicate results?",
    option1="UNIQUE",
    option2="DISTINCT",
    option3="DIFFERENT",
    option4="FILTER",
    answer="DISTINCT"
),


# =====================
# C PROGRAMMING
# =====================

Question(
    category="C",
    question="Who developed C language?",
    option1="James Gosling",
    option2="Dennis Ritchie",
    option3="Bjarne Stroustrup",
    option4="Guido van Rossum",
    answer="Dennis Ritchie"
),

Question(
    category="C",
    question="Which function is the starting point?",
    option1="start()",
    option2="main()",
    option3="begin()",
    option4="run()",
    answer="main()"
),

Question(
    category="C",
    question="Which symbol ends a statement?",
    option1=":",
    option2=".",
    option3=";",
    option4=",",
    answer=";"
),

Question(
    category="C",
    question="Which header is used for printf()?",
    option1="stdlib.h",
    option2="stdio.h",
    option3="string.h",
    option4="math.h",
    answer="stdio.h"
),

Question(
    category="C",
    question="Which operator gets the address?",
    option1="*",
    option2="&",
    option3="#",
    option4="%",
    answer="&"
),

Question(
    category="C",
    question="Which data type stores a character?",
    option1="char",
    option2="string",
    option3="character",
    option4="text",
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
    option1="return",
    option2="send",
    option3="result",
    option4="output",
    answer="return"
),


# =====================
# DATA STRUCTURES
# =====================

Question(
    category="Data Structures",
    question="Which data structure follows LIFO?",
    option1="Queue",
    option2="Stack",
    option3="Array",
    option4="Tree",
    answer="Stack"
),

Question(
    category="Data Structures",
    question="Which data structure follows FIFO?",
    option1="Stack",
    option2="Queue",
    option3="Tree",
    option4="Graph",
    answer="Queue"
),

Question(
    category="Data Structures",
    question="Which structure consists of nodes and edges?",
    option1="Array",
    option2="Stack",
    option3="Graph",
    option4="Queue",
    answer="Graph"
),

Question(
    category="Data Structures",
    question="Which search works on sorted data?",
    option1="Linear Search",
    option2="Binary Search",
    option3="Random Search",
    option4="Sequential Search",
    answer="Binary Search"
),

Question(
    category="Data Structures",
    question="What is the root node of a tree?",
    option1="Last node",
    option2="First/top node",
    option3="Leaf node",
    option4="Middle node",
    answer="First/top node"
),

Question(
    category="Data Structures",
    question="Which structure uses nodes connected by links?",
    option1="Linked List",
    option2="Array",
    option3="Matrix",
    option4="Hash",
    answer="Linked List"
),


# =====================
# DBMS
# =====================

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
    question="Which is a database model?",
    option1="Relational",
    option2="Circular",
    option3="Linear",
    option4="Sequential",
    answer="Relational"
),

Question(
    category="DBMS",
    question="What is a collection of related data?",
    option1="Database",
    option2="Program",
    option3="Algorithm",
    option4="File",
    answer="Database"
),

Question(
    category="DBMS",
    question="Which key links two tables?",
    option1="Primary Key",
    option2="Foreign Key",
    option3="Unique Key",
    option4="Super Key",
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


# =====================
# HTML/CSS
# =====================

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
)

]


with app.app_context():

    db.session.add_all(questions)

    db.session.commit()

    print(
        f"{len(questions)} questions added successfully!"
    )