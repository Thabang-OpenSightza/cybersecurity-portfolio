from flask import Flask, request

app = Flask(__name__)

# VULNERABILITY 1: Hardcoded Secret (CWE-798)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLEwJalrXUtnFEMI/K7MDENG/bPxRfiCY"
DB_PASSWORD = "SuperSecretPassword123!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
       
    # VULNERABILITY 2: SQL Injection (CWE-89)
    # A secure app would use parameterized queries, not string concatenation.
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
       
    return f"Executing query: {query}"

if __name__ == '__main__':
    app.run(debug=True)