import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USERS_DB = os.path.join(BASE_DIR, "users.db")
def get_users_db():

    connection = sqlite3.connect(
        USERS_DB
    )

    connection.row_factory = sqlite3.Row

    return connection


def init_users_db():

    connection = get_users_db()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_logged_in INTEGER DEFAULT 0
        )
        """
    )

    connection.commit()

    cursor.close()

    connection.close()
init_users_db()    
if __name__ == "__main__":
    app.run(debug=True)