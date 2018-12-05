from app import app, db
from app.models import User, Post
from flask_login import current_user
from datetime import datetime


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
