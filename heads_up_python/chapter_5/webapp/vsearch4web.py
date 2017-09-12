from flask import Flask, render_template, request, session
from vsearch import search_for_letters
from DBcm import UseDatabase
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecret'

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'root',
                          'password': '',
                          'database': 'vsearchlogDB', }


def log_request(req: 'flask_request', res: str) -> None:
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """INSERT INTO log
              (phrase, letters, ip, broswer_string, results)
              VALUES
              (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'You are logged in'


@app.route('/logout')
def logout() -> str:
    session.pop('logged_in')
    return 'You are logged out'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    title = 'Here are your results:'
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_results=results,
                           the_letters=letters,
                           the_phrase=phrase, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """SELECT phrase, letters, ip, broswer_string, results
                  FROM log;"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
