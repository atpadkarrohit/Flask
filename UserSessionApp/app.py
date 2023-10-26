from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Configure Flask-Session to use the 'filesystem' type of session storage.
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    if 'user_data' in session:
        user_data = session['user_data']
    else:
        user_data = 'No user data available.'

    return render_template('index.html', user_data=user_data)

@app.route('/set_session', methods=['POST'])
def set_session():
    if request.method == 'POST':
        user_data = request.form['user_data']
        session['user_data'] = user_data
    return redirect(url_for('home'))

@app.route('/clear_session')
def clear_session():
    session.pop('user_data', None)
    return redirect(url_for('home'))

if __name__ == '__main__' :
    app.run(host="0.0.0.0",port=5002)
 



