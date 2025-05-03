import os
from flask import Flask, request
from flask_cors import CORS
from .models import db

# ── ABSOLUTE path to  <repo>/server/instance/db.sqlite3 ─────────────────────
BASE_DIR     = os.path.abspath(os.path.dirname(__file__))       # …/server
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
DB_PATH      = os.path.join(INSTANCE_DIR, "db.sqlite3")
os.makedirs(INSTANCE_DIR, exist_ok=True)
# ─────────────────────────────────────────────────────────────────────────────

def create_app():
    # hard-wire Flask to that folder
    app = Flask(
        __name__,
        instance_path=INSTANCE_DIR,        # ← THIS forces server/instance
        instance_relative_config=False
    )

    app.config.update(
        SECRET_KEY="naum-secret-key",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{DB_PATH}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    #CORS(app)
    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"],   # ← exact casing
        expose_headers=["Content-Type"],
        max_age=3600,
    )

    print("📂 DB URI →", app.config["SQLALCHEMY_DATABASE_URI"])

    from .auth  import auth_bp
    from .tasks import tasks_bp
    app.register_blueprint(auth_bp,  url_prefix="/api/auth")
    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")

    @app.before_request
    def _trace():
        print(f"[TRACE] {request.method} {request.path}")

    return app


if __name__ == "__main__":
    create_app().run(debug=False)    # turn off auto-reload to avoid confusion
