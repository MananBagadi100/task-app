# NAUM Task Management App

## Overview

This is a full‑stack task management application built with a Flask REST API backend and a React + Vite + Tailwind CSS frontend. Users can register, log in, and manage their personal tasks (create, view, update status, delete, and filter by status and priority).

---

## 📁 Repository Structure

```
Naum-task-app/
├── client/                # React frontend (Vite + Tailwind)
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── api/           # Axios instance (api/axios.js)
│   │   ├── components/    # Reusable UI: TaskRow.jsx, TaskForm.jsx
│   │   ├── hooks/         # Custom hooks: useAuth.js
│   │   ├── pages/         # Routes: Login.jsx, Dashboard.jsx
│   │   ├── App.jsx        # Routes & layout
│   │   ├── main.jsx       # Entry point
│   │   └── index.css      # Tailwind imports
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── server/                # Flask backend
│   ├── backend-env/       # Python virtual environment
│   ├── instance/          # SQLite database file (db.sqlite3)
│   ├── __init__.py        # Package marker
│   ├── app.py             # Factory, config, CORS, blueprint registration
│   ├── models.py          # SQLAlchemy models: User, Task
│   ├── auth.py            # Authentication blueprint (register/login/debug)
│   ├── tasks.py           # Task CRUD blueprint
│   ├── utils.py           # token_required decorator
│   ├── seed.py            # Seed script for test users & tasks
│   └── requirements.txt   # Python dependencies
│
└── README.md              # You are here
```

---

## ⚙️ Setup Instructions

### Prerequisites

* Python 3.8+ and pip
* Node.js (v16+) and npm

### Backend

1. **Navigate** to server folder:

   ```bash
   cd server
   ```
2. **Create & activate** Python venv, install dependencies:

   ```bash
   python3 -m venv backend-env
   source backend-env/bin/activate
   pip install -r requirements.txt
   ```
3. **Seed** the database with test users & tasks:

   ```bash
   python -m server.seed
   ```
4. **Run** the Flask app (serves on port 5000):

   ```bash
   python -m server.app
   # API base URL: http://127.0.0.1:5000/api
   ```

### Frontend

1. **Navigate** to client folder:

   ```bash
   cd client
   ```
2. **Install** dependencies and start dev server (serves on port 5173):

   ```bash
   npm install
   npm run dev
   ```
3. **Open** your browser and visit:

   ```
   http://localhost:5173
   ```

---

## 🏗️ Architecture & Technical Choices

* **Backend**

  * Flask application factory (`create_app`) with SQLAlchemy integration (`db.init_app`).
  * Modular routes using Blueprints (`auth_bp`, `tasks_bp`).
  * JWT (PyJWT) for stateless authentication.
  * `token_required` decorator to protect endpoints.
  * CORS configured to allow frontend origin (default `*`).
  * SQLite for simplicity; file located at `server/instance/db.sqlite3`.

* **Frontend**

  * React functional components + Hooks (`useState`, `useEffect`).
  * Vite for fast development builds.
  * Tailwind CSS for utility‑first styling.
  * Axios for HTTP requests to backend.
  * React Router for client‑side routing.
  * Custom hook `useAuth` for authentication logic & token management.

---

## 💾 Database Schema

### User

| Column   | Type    | Constraints                 |
| -------- | ------- | --------------------------- |
| id       | Integer | PK, auto‑increment          |
| email    | String  | Unique, not null            |
| password | String  | Hashed (Werkzeug), not null |

### Task

| Column      | Type        | Constraints                         |
| ----------- | ----------- | ----------------------------------- |
| id          | Integer     | PK, auto‑increment                  |
| title       | String(120) | Not null                            |
| description | Text        | Nullable                            |
| status      | String(20)  | Default 'incomplete'                |
| priority    | String(20)  | Default 'Low'                       |
| created_at  | DateTime    | Default UTC now                     |
| user_id     | Integer     | FK → User.id (tasks belong to user) |

---

## 🧪 Seed Data

The seed script (`seed.py`) creates two users with sample tasks:

1. **[manan@example.com](mailto:manan@example.com)** / `password123`
2. **[deepak@example.com](mailto:deepak@example.com)** / `password123`

Each user will have 2–3 tasks seeded for testing. Run the seed script to recreate or refresh data:

```bash
python -m server.seed
```

---

## 🚀 Running the Application Locally

1. Start **Backend** on port 5000:

   ```bash
   cd server && source backend-env/bin/activate
   python -m server.app
   ```
2. Start **Frontend** on port 5173:

   ```bash
   cd client
   npm run dev
   ```
3. **Login** with one of the seed users (e.g., `manan@example.com` / `password123`).
4. **Use** the UI to add, toggle, delete, and filter tasks by status and priority.

---

## 📄 License & Submission

* Push to a Github repository and share the link.
* Update this README specific notes.
* Include seed data and sample user credentials for evaluation.

Happy coding! 🎉
