from flask import render_template, flash, url_for, redirect, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from flask_login import login_required
from app import db
from app.forms import RegistrationForm
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required   # this url becomes protected with user requiring login to see it
def index():
    # render_template invokes jinja2 template engine
    return render_template('index.html', title='Home')
    # return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # identify if user is already authenticated, and if so redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # method validate_on_submit does the processing, GET will return false, skipping if statement
        # POST submit is going to gather data, run validators, and return True, ready to be processed
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)  # , remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            # if there is not a next in the url or if the url is to a different domain, then redirect to index
            next_page = url_for('index')
        return redirect(next_page)  # otherwise redirect to the next page
    return render_template('login.html', title='Signin', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, twofact=form.twofact.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)