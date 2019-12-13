from flask import render_template
from app import app

@app.route('/')
@app.route('/index')


def index():
    user = {'username':'Rob'}
    posts = [
        {
            'author': {'username': 'Brad'},
            'body': 'I love flask!'
        },
        {
            'author': {'username': 'Jerry'},
            'body': 'Tom!'
        }
    ]
    # render_template invokes jinja2 template engine
    return render_template('index.html', title='Home', user=user, posts=posts)