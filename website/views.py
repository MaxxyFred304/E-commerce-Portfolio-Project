from flask import Blueprint
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/products')
def products():
    return render_template('product.html')

@views.route('/products/laptop')
def laptop():
    return render_template('laptop.html')

@views.route('/products/computer')
def computer():
    return render_template('computer.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
    # Handle user login logic here (e.g., form validation, authentication)
    if request.method == 'POST':
        # Process the submitted form data and authenticate the user
        # You can add your login logic here

        # If authentication is successful, redirect to a protected page
        return redirect(url_for('protected_page'))

    # If the request method is GET or authentication failed, render the login template
    return render_template('login.html')




