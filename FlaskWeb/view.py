from flask import Blueprint, render_template,request

views = Blueprint('view', __name__)


@views.route('/')
def home_page():
    return render_template('home.html')

# @views.route('/login',methods=['GET','POST'])
# def login_page():
#     email = request.form['Email']
#     password = request.form['Password']

@views.route('/work')
def work_page():
    return render_template('work.html')

@views.route('/about')
def about_page():
    return render_template('about.html')

@views.route('/work/price')
def price_page():
    return render_template('price.html')

@views.route('/work/contact')
def contact_page():
    return render_template('contact.html')