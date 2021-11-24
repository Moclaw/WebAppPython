from flask import Blueprint, render_template, request, flash
import re
import sqlite3

import flask

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')

@auth.route("/logout")
def logout_page():
    return "<p>logout</p>"


@auth.route("/regist", methods=['GET', 'POST'])
def regist_page():
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password = request.form.get('password1')
        password_confirm = request.form.get('password2')

        if len(email) < 12:
            flash('This is not mail, try again!', category='error')
        elif len(first_name) < 2:
            flash('No one  have a First Name have 2 character, Bro get some char pls!!', category='error')
            if re.search("[0-9]",first_name):
                flash('Serious? Name have number??', category='error')
        elif len(last_name) < 2:
            flash('No one  have a Last Name have 2 character, Bro get some char pls!!', category='error')
            if re.search("[0-9]",first_name):
                flash('Serious? Name have number??', category='error')
        elif password != password_confirm:
            flash('Password don\'t match', category='error')
            if len(password) < 6 or len(password_confirm) < 6:
                if regex.search(password) != None and regex.search(password_confirm) != None:
                    flash('Your password too strong, so I can\'t let you through', category='error')
                    if password.islower() or password_confirm.islower():
                        flash('Your password too strong, so I can\'t let you through', category='error')
                    return
        else:
            flash('Account created!', category='success')

        conn = sqlite3.connect('WebAppPython/account.db')
        cur = conn.cursor()
        arg = request.form
        email = arg['email']
        name = arg['lastName'] + ' ' + arg['firstName']
        password = arg['password1']
        check = conn.execute(f"SELECT * FROM user WHERE email = '{email}'")
        result= check.fetchall()
        if result == []:
            conn.execute(f"INSERT INTO user VALUES ('{name}','{password}','{email}')")
        else:
            flash('Account already exists',category='error')
        conn.commit()
        conn.close()
        
    return render_template('regist.html')
