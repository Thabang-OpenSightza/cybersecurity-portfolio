from flask import Flask, request
import os

app = Flask(__name__)

# SECURE: Useing environment variables instead of hardcoded secrets
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # SECURE: Useing parameterized queries to prevent SQL injection
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    params = (username, password)
    
    return f"Executing secure query with parameters"

if __name__ == '__main__':
    app.run(debug=False)