## 🧭 Project Overview
The **Job Search Website** is a **Flask-based web application** that connects job seekers and employers through a machine learning–driven platform.  
It features an ML model that automatically recommends suitable job categories based on job titles and descriptions, reducing manual errors and improving exposure to relevant candidates.

This project was completed for **RMIT University’s Advanced Programming for Data Science** course and developed in two milestones:
1. **Milestone I:** Built ML models to classify job advertisements into categories.  
2. **Milestone II:** Integrated the trained model into a Flask web application.

---

## ✨ Key Highlights
- 🔍 **Intelligent Search:** Flexible keyword-based job search (e.g., “work”, “worked”, “working”).  
- 🧠 **AI-Powered Recommendations:** Category suggestions using a pre-trained model (`descFT_LR.pkl`).  
- 🏢 **Dual Functionality:** Supports both job seekers and employers.  
- 🎨 **Modern Frontend:** Built with HTML, CSS, Bootstrap, and Jinja2 templates.  
- ⚙️ **End-to-End Deployment:** Combines Flask backend, ML inference, and dynamic UI.

---

## 🧰 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python 3 |
| **Web Framework** | Flask |
| **Machine Learning** | Scikit-learn, Pickle |
| **Data Handling** | pandas, numpy |
| **Frontend** | HTML5, CSS3, Bootstrap, Jinja2 |
| **Environment** | VS Code / Jupyter Notebook |

---

## 🗂️ Project Structure

| File / Folder | Description |
|----------------|--------------|
| `app.py` | Main Flask backend handling routes, logic, and ML predictions |
| `templates/` | HTML pages (Home, Search, Job Details, Post Job) |
| `static/` | CSS and static assets |
| `data/` | Job data and trained model files |
| `descFT_LR.pkl` | Pre-trained ML model for job category classification |
| `styles.css` | Custom frontend styling |

---

## 👨‍💻 Features

### 🔹 For Job Seekers
- Search jobs by keyword or skill set.  
- View summarized listings and detailed descriptions.  
- Smart query matching for synonyms and variations.

### 🔹 For Employers
- Post new job listings with title, description, salary, and category.  
- Get **ML-powered job category recommendations** instantly.  
- Edit or override suggested categories as needed.

---
