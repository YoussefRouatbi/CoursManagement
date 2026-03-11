# 📚 CoursManagement

A modern **Course Management Web Application** built with **Svelte, TailwindCSS, Python (Flask), and MySQL**.
This project provides a structured platform for managing courses, users, and educational resources through a clean web interface and REST API backend.

---

# 🚀 Project Overview

**CoursManagement** is a full-stack web application designed to help organize and manage educational content.

The system allows administrators or teachers to manage:

* Courses
* Users
* Educational resources
* Course materials

The frontend provides a modern UI built with **Svelte and Tailwind**, while the backend uses **Flask APIs** connected to a **MySQL database**.

---

# 🧰 Tech Stack

### Frontend

* **Svelte**
* **TailwindCSS**
* **Vite**

### Backend

* **Python**
* **Flask (REST API)**

### Database

* **MySQL**

---

# ✨ Features

📚 Course management
👤 User management
🔐 Backend API with Flask
⚡ Fast frontend with Svelte
🎨 Modern UI with TailwindCSS
🗄 MySQL database integration

---

# 📂 Project Structure

```
CoursManagement
│
├── database          # Database schema / SQL files
│
├── public            # Static assets
│
├── routes            # Backend API routes (Flask)
│
├── src               # Svelte frontend source code
│
├── dist              # Production build
│
├── venv              # Python virtual environment
│
├── index.html        # Frontend entry point
│
├── package.json      # Node dependencies
│
├── vite.config.js    # Vite configuration
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/YoussefRouatbi/CoursManagement.git
cd CoursManagement
```

---

## 2️⃣ Setup Python Environment

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install flask mysql-connector-python
```

---

## 3️⃣ Setup Frontend

Install Node dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

---

## 4️⃣ Configure MySQL

Create the database:

```sql
CREATE DATABASE coursmanagement;
```

Update your database connection inside the Flask backend.

---

# 🧪 Running the Project

Start the backend server:

```bash
python app.py
```

Run the frontend:

```bash
npm run dev
```

Then open:

```
http://localhost:5173
```

---

# 🎯 Project Purpose

This project was created to practice **full-stack development** using modern tools and frameworks.
It demonstrates how to integrate:

* A modern frontend framework
* A Python backend API
* A relational database
* A clean project architecture

---

# 🛠 Future Improvements

Possible future features:

* Authentication system
* Role-based access (Admin / Student)
* Course enrollment
* File upload for course materials
* Dashboard analytics

---

# 👨‍💻 Authors

**Youssef Rouatbi**
**Habib Trabelsi**

🎓 Computer Science Students — *Bac Informatique*
💻 Interested in **Backend Development, AI, and Software Engineering**

GitHub:
https://github.com/YoussefRouatbi
https://github.com/habib13564

---

⭐ If you find this project useful, consider giving it a **star**!
