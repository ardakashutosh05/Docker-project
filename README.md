# 🚀 Docker DevOps Project (Full Stack + CI/CD + AWS)

## 📌 Project Overview

This project demonstrates a **production-style DevOps setup** using Docker.
It includes a multi-container application with:

* Backend API (Flask)
* Database (PostgreSQL)
* Cache (Redis)
* Reverse Proxy (Nginx)
* CI/CD Pipeline using GitHub Actions
* Deployment on AWS EC2

---

## 🧱 Architecture

User → Nginx → Backend → Redis → PostgreSQL

---

## ⚙️ Tech Stack

* Python (Flask)
* Docker & Docker Compose
* Nginx
* PostgreSQL
* Redis
* GitHub Actions (CI/CD)
* AWS EC2

---

## 📁 Project Structure

```
docker-project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf
│
├── docker-compose.yml
├── .github/workflows/docker.yml
├── deploy.sh
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Clone Repository

```
git clone <your-repo-url>
cd docker-project
```

### 2. Run with Docker Compose

```
docker-compose up --build
```

---

## 🌐 Access Application

* Application: http://localhost
* Backend (direct): http://localhost:5000

---

## 🔥 Features

* Multi-container Docker setup
* Service-to-service communication using Docker network
* Persistent database using volumes
* Redis caching for fast responses
* Nginx reverse proxy (production setup)
* CI/CD pipeline using GitHub Actions
* Auto deployment on AWS EC2

---

## 🔄 CI/CD Pipeline

Using GitHub Actions:

* Build Docker image
* Push to Docker Hub
* Deploy to AWS EC2 via SSH

---

## ☁️ AWS Deployment

* Hosted on AWS EC2 instance
* Docker installed on EC2
* Automatic deployment using CI/CD

---

## 🧠 Key Concepts Covered

* Dockerfile creation
* Docker Compose orchestration
* Container networking (service name communication)
* Volumes for data persistence
* Reverse proxy using Nginx
* Redis caching
* CI/CD automation
* Cloud deployment

---

## 💣 Challenges Faced

* Docker Compose errors (volume & YAML issues)
* Container networking (localhost vs service name)
* Dependency installation issues
* AWS security group configuration
* CI/CD secrets handling

---

## 🎯 Learning Outcome

* Built a real-world DevOps project from scratch
* Understood container orchestration
* Implemented CI/CD pipeline
* Deployed application on cloud (AWS)

---

## 👨‍💻 Author

Ashutosh (Jannu)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

