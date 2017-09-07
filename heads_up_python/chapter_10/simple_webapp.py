from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecret'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'You are logged in'


@app.route('/logout')
def logout() -> str:
    session.pop('logged_in')
    return 'You are logged out'


@app.route('/status')
def status() -> str:
    if 'logged_in' in session:
        return 'You are logged in'
    return 'You are not logged in'


@app.route('/page1')
def page1() -> str:
    return 'This is page1.'


@app.route('/page2')
def page2() -> str:
    return 'This is page2.'


@app.route('/page3')
def page3() -> str:
    return 'This is page3.'


if __name__ == '__main__':
    app.run(debug=True)

