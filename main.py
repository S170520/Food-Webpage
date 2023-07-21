from flask import Flask, render_template, request, redirect, url_for, session
from replit import db

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] in db["Users"] and db["Users"][request.form['username']] == request.form['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password. Please try again.'
    else:
        return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    new_username = request.form['new_username']
    new_password = request.form['new_password']
    db["Users"][new_username] = new_password
    print('Registration successful!')
    return render_template('index.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
