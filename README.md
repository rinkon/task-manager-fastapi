# 📝 Task Manager API (FastAPI + JWT)

A production-style backend API built with **FastAPI**, featuring **JWT authentication, user-specific task management, and clean architecture principles**.

---

## 🚀 Features

* 🔐 JWT Authentication (Register/Login)
* 👤 User-based task ownership
* 📝 Full CRUD for tasks
* 🛡️ Protected routes (authorization)
* 🧱 Modular architecture (routes, core, models, services, db, schemas)
* ⚡ FastAPI auto docs (`/docs`)
* 🐳 Docker support
* 🧪 Unit tests 

---

## 🏗️ Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL (configurable)
* JWT (python-jose)
* argon2 (password hashing)
* uvicorn
* Docker
* Pytest

---

## 📁 Project Structure

```
app
 ┣ api
 ┃ ┣ routes
 ┃ ┃ ┣ auth.py
 ┃ ┃ ┗ tasks.py
 ┃ ┗ deps.py
 ┣ core
 ┃ ┣ config.py
 ┃ ┣ hashing.py
 ┃ ┗ security.py
 ┣ db
 ┃ ┣ base.py
 ┃ ┗ database.py
 ┣ models
 ┃ ┣ task.py
 ┃ ┗ user.py
 ┣ schemas
 ┃ ┣ tasks.py
 ┃ ┗ user.py
 ┣ services
 ┃ ┣ auth_service.py
 ┃ ┗ task_service.py
 ┣ tests
 ┃ ┣ conftest.py
 ┃ ┗ test_auth.py
 ┃ ┗ test_tasks.py
 ┣ utils
 ┗ main.py
```

---

## 🔐 Authentication Flow

1. User registers (`/auth/register`)
2. User logs in (`/auth/login`)
3. Server returns JWT token
4. Token is used in `Authorization: Bearer <token>`
5. Protected routes validate user identity

---

## 📌 API Endpoints

### Auth

* `POST /auth/register` → Create user
* `POST /auth/login` → Get JWT token

### Tasks

* `POST /tasks` → Create task
* `GET /task/{id}` → Get task by ID
* `GET /tasks` → Get all user tasks
* `PUT /tasks/{id}` → Update task
* `DELETE /tasks/{id}` → Delete task

---

## ▶️ Run Locally

### 1. Clone repo

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run server

```bash
uvicorn app.main:app --reload
```

---

## 🐳 Run with Docker

### Build image

```bash
docker build -t task-manager-api .
```

### Run container

```bash
docker compose up -d 
```

---

## 📖 API Docs

Once running, visit:

* Swagger UI → http://localhost:8000/docs
* ReDoc → http://localhost:8000/redoc

---

## 🧠 Important Dev features

* JWT authentication flow
* Dependency injection in FastAPI
* Service-layer architecture
* Database modeling with SQLAlchemy
* Dockerizing backend applications

---

## 🔥 Future Improvements

* PostgreSQL + Alembic migrations
* Role-based access (admin/user)
* Pagination & filtering
* Refresh tokens
* CI/CD pipeline
* Deployment (Render / AWS)

---

## 📌 Author

Built as a FastAPI learning + portfolio project.
