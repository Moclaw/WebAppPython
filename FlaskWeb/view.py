from flask import Blueprint, render_template

views = Blueprint('view', __name__)


@views.route('/')
def home_page():
    return render_template('home.html')

@views.route('/work')
def work_page():
    return render_template('work.html')

@views.route('/about')
def about_page():
    return render_template('about.html')

@views.route('/work/worksingle')
def work_single_page():
    return render_template('work-single.html')

@views.route('/work/price')
def price_page():
    return render_template('price.html')

@views.route('/work/contact')
def contact_page():
    return render_template('contact.html')