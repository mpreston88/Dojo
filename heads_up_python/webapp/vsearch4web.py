from flask import Flask, render_template, request
from vsearch import search_for_letters


app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))
    title = 'Here are your results:'
    return render_template('results.html',
                           the_title=title,
                           the_results=results,
                           the_letters=letters,
                           the_phrase=phrase,
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run(debug=True)
