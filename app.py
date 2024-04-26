"""
Starts a web flask app.

This module initializes a Flask application and defines a route for the homepage.
It also configures a SQLite database using SQLAlchemy.

Attributes:
    app (Flask): The Flask application object.
    db (SQLAlchemy): The SQLAlchemy database object.

"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    """
    Defines the route for the homepage.

    Returns:
        The rendered template for the index.html page.
    """
    return render_template('home.html')

@app.route('/blog')
def blog():
    """
    Renders the blog.html template.

    Returns:
        The rendered blog.html template.
    """
    return render_template('blog.html')

@app.route('/portfolio')
def portfolio():
    """
    Renders the portfolio.html template.

    Returns:
        The rendered portfolio.html template.
    """
    return render_template('portfolio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Handle the contact form submission.

    If the request method is POST, retrieve the name, email, and message from the form data.
    Print the name, email, and message to the console.
    Return a rendered template for the contact confirmation page with the name passed as a parameter.

    If the request method is not POST, return a rendered template for the contact page.

    Returns:
        A rendered template for either the contact confirmation page or the contact page.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return render_template('contact_confirmation.html', name=name)
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)
