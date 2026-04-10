from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database and table
conn = sqlite3.connect('students.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT
)
''')

conn.commit()
conn.close()


@app.route('/')
def home():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )

    conn.commit()
    conn.close()

    return render_template('success.html', name=name)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)