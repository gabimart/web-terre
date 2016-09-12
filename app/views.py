# coding: utf-8

from app import app, lm
from models import User
from flask import render_template, redirect, url_for, request, flash
from app.forms import LoginForm
from flask_login import login_user, logout_user


@app.route('/login', methods=['GET', 'POST',])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if user.is_correct_password(form.password.data):
                login_user(user)
                return 'User loged'
            else:
                flash('Espabila....Mete bien la contraseña....')
                return redirect(url_for('login'))
        else:
            flash('Espabila....Mete bien tu nombre de usuario....')
            return redirect(url_for('login'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@lm.user_loader
def load_user(userid):
    return User.query.filter(User.username==userid).first()