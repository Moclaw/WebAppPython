from flask import Blueprint, render_template, request, flash
import re

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', boolean=True)


@auth.route("/logout")
def logout():
    return "<p>logout</p>"


@auth.route("/register", methods=['GET', 'POST'])
def signin():
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password = request.form.get('password1')
        password_confirm = request.form.get('password2')
        if len(email) < 3:
            flash('This is not mail, try again!', category='error')
        elif len(first_name) <= 2:
            flash('No one  have a First Name have 2 character, Bro get some char pls!!', category='error')
            if not first_name.isalpha():
                flash('Serious? Name have number??', category='error')
        elif len(last_name) <= 2:
            flash('No one  have a Last Name have 2 character, Bro get some char pls!!', category='error')
            if not last_name.isnumeric():
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
        print(request.form)
    return render_template('register.html')
