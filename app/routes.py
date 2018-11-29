# coding:'utf-8'

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mikhail'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Poland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
