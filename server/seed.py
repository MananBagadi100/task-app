# server/seed.py
"""
Seed script: drops all tables, recreates them, and inserts demo data.
Run with:  python -m server.seed
"""
from werkzeug.security import generate_password_hash
from .app    import create_app          # ← dotted import = inside same package
from .models import db, User, Task


def run_seed() -> None:
    app = create_app()

    with app.app_context():
        # fresh slate
        db.drop_all()
        db.create_all()

        # demo users
        u1 = User(
            email="manan@example.com",
            password=generate_password_hash("password123"),
        )
        u2 = User(
            email="deepak@example.com",
            password=generate_password_hash("password123"),
        )
        db.session.add_all([u1, u2])

        # demo tasks
        tasks = [
            Task(title="Buy milk",          priority="Low",    user=u1),
            Task(title="Finish report",     priority="High",   user=u1),
            Task(title="Book flight ticket", priority="Medium", user=u2),
        ]
        db.session.add_all(tasks)

        db.session.commit()
        print("✅  Seed complete – 2 users & 3 tasks added.")


if __name__ == "__main__":
    run_seed()