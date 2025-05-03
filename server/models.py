# server/models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# ── single, global SQLAlchemy instance ──
db = SQLAlchemy()


# ── USER ─────────────────────────────────────────────────────────────────────
class User(db.Model):
    __tablename__ = "users"

    id       = db.Column(db.Integer, primary_key=True)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256),               nullable=False)

    # 1-to-many: user → tasks
    tasks    = db.relationship(
        "Task",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<User {self.email}>"


# ── TASK ──────────────────────────────────────────────────────────────────────
class Task(db.Model):
    __tablename__ = "tasks"

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    status      = db.Column(db.String(20),  default="incomplete")  # complete / incomplete
    priority    = db.Column(db.String(20),  default="Low")         # Low / Medium / High
    created_at  = db.Column(db.DateTime,   default=datetime.utcnow)

    user_id     = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Task {self.title} ({self.status})>"

'''
from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='incomplete')  # 'complete' or 'incomplete'
    priority = db.Column(db.String(20), default='Low')  # Low, Medium, High
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title} ({self.status})>'
'''