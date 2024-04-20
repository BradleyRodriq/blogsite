""" user auth """
from flask_login import UserMixin, LoginManager
from app import app, db

app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    """Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        password (str): The password of the user.

    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    """Loads user data based on the given user_id.

    Args:
        user_id (int): The ID of the user to load.

    Returns:
        User: The user object corresponding to the user_id.

    """
    return User.query.get(int(user_id))
