# HNG-DevOps-One

A simple personal API built and deployed as part of a DevOps learning task.
It exposes basic identity and health endpoints and is served behind an Nginx reverse proxy.

---

##  Overview

This project demonstrates:

* Building a lightweight API
* Running a backend service on a private port
* Exposing it securely using **Nginx reverse proxy**
* Keeping the service alive using a process manager

---

##  Tech Stack

* **Backend:** FastAPI (Python)
* **Server:** Gunicorn
* **Reverse Proxy:** Nginx
* **Process Manager:** systemd
* **Infrastructure:** VPS (Linux)

---

## 🧪 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nehecodes/hng-devops-one.git
cd hng-devops-one
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn
```

### 3. Start the server

```bash
uvicorn main:app --reload
```

### 4. Test endpoints

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/me
```

---

##  API Endpoints

### `GET /`

```json
{
  "message": "API is running"
}
```

### `GET /health`

```json
{
  "message": "healthy"
}
```

### `GET /me`

```json
{
  "name": "Nehemiah Adoba Daniel",
  "email": "you@example.com",
  "github": "https://github.com/yourusername"
}
```

---

##  Live Deployment

Base URL:

```
http://your-server-ip/
```

Example:

```bash
curl http://your-server-ip/me
```