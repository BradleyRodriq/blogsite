""" database values """
from flask_sqlalchemy import SQLAlchemy
from app import app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    """
    Represents a blog post.

    Attributes:
        id (int): The unique identifier for the blog post.
        title (str): The title of the blog post.
        content (str): The content of the blog post.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Project(db.Model):
    """
    Represents a project in the blogsite.

    Attributes:
        id (int): The unique identifier for the project.
        title (str): The title of the project.
        description (str): The description of the project.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class ContactSubmission(db.Model):
    """
    Represents a contact submission.

    Attributes:
        id (int): The unique identifier for the contact submission.
        name (str): The name of the person submitting the contact form.
        email (str): The email address of the person submitting the contact form.
        message (str): The message content of the contact submission.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
