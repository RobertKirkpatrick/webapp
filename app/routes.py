from flask import render_template, flash, url_for, redirect
from app import app
from app.forms import LoginForm

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #method validate_on_submit does the processing, GET will return false, skipping if statement
        # POST submit is going to gather data, run validators, and return True, ready to be processed
        #on TRUE, two functions are called, flash() to let the user know an action was succesfull and redirect()
        flash('Login requested for user {}'.format(form.username.data)) #add 2factor here****
        return redirect(url_for('index'))
    return render_template('login.html', title='Signin', form=form)