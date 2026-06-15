# 🔐 Caesar Cipher Web App (Flask)

A modern multi-page web application built using Python Flask that implements the classic Caesar Cipher encryption technique.  
This project allows users to encrypt and decrypt messages, maintain history logs, and learn how the cipher works through an interactive UI.

---

## 🚀 Features

- 🔐 Encrypt and Decrypt messages instantly
- 📜 Stores recent history (last 25 actions)
- 🧠 Multi-page educational structure
- ⚡ Flask REST API backend
- 🎨 Modern cyber-themed UI design
- 📱 Fully responsive layout
- 🗑 Clear history functionality
- 📊 Live status updates
- 🌐 Smooth navigation between pages

---

## 🧱 Project Structure

caesar-cipher-flask/
│
├── app.py
├── requirements.txt
├── history.json
│
├── templates/
│   ├── index.html
│   ├── cipher.html
│   ├── history.html
│   ├── about.html
│   ├── working.html
│   └── contact.html
│
└── static/
    ├── style.css
    └── script.js

---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/your-username/caesar-cipher-flask.git
cd caesar-cipher-flask

### 2. Create virtual environment (recommended)
python -m venv venv

Activate:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the application
python app.py

### 5. Open in browser
http://127.0.0.1:5000

---

## 🔐 How Caesar Cipher Works

Caesar Cipher is one of the oldest encryption techniques where each letter in the message is shifted by a fixed number.

Example:

Plain Text : HELLO
Shift : 3
Cipher Text: KHOOR

---

## 📊 Formula

(ASCII value + shift) mod 26

---

## 📜 History Feature

This project automatically stores user activity.

### Each log includes:

Input message
Shift value
Action (Encrypt / Decrypt)
Output result
Timestamp

### Stored in:

### history.json
🧠 Tech Stack
Python 🐍
Flask 🌐
HTML5
CSS3
JavaScript
JSON (for data storage)

---

## 🎯 Learning Outcomes
Basics of Cryptography
Flask web development
API creation and handling
Frontend + Backend integration
Multi-page web application design
File-based storage system

---

## 🎨 UI Highlights
Animated gradient background
Glassmorphism design
Cybersecurity-inspired theme
Smooth transitions & hover effects
Responsive mobile-friendly layout

---

## 🔮 Future Improvements
User authentication system
Download history as PDF
Dark/Light mode toggle
Encryption strength visualization
Cloud deployment (Render / Railway / PythonAnywhere)
API integration mode (Postman support)

---

## 👨‍💻 Author
Dhvani
Student | Developer | Cybersecurity Enthusiast
Focused on Web Development & Ethical Hacking
