# 💼 Data Engineer Portfolio

Welcome to my personal Data Engineer portfolio website! This project showcases my experience, projects, and skills in data engineering — all in a modern, interactive way using **Streamlit**.

> 🔗 Live Website: [Visit Portfolio](https://data-engineer-portfolio-mmi4cg2uujzcu6zo6rf6ga.streamlit.app)  
> 📄 Thank You Page: [View Thank You](https://mukeshdt.github.io/data-engineer-portfolio/thankyou.html)

---

## 📌 Project Overview

This project was created to:
- Present a clean and responsive personal website
- Showcase hands-on data engineering projects
- Provide a downloadable resume
- Enable recruiters to contact me directly via a built-in form
- Demonstrate deployment and automation via GitHub & Streamlit Cloud

---

## ⚙️ Tech Stack

| Tool         | Description                         |
|--------------|-------------------------------------|
| **Streamlit**| Web framework for data apps         |
| **HTML/CSS** | Custom thank-you page               |
| **Python**   | Main programming language           |
| **GitHub**   | Version control & repo management   |
| **GitHub Pages** | Hosting for static thank-you page |
| **Streamlit Cloud** | Free deployment of the portfolio app |

---

## 🧩 Features

✅ Home with Introduction  
✅ About Section with Photo and Bio  
✅ Projects with Descriptions and Tech Stack  
✅ Resume Download Button  
✅ Contact Form with Email Sending  
✅ Custom HTML Thank You Page with Redirection  
✅ Mobile Responsive and Clean Design  
✅ Professional Color Scheme

---

## 🚀 How It Works

### 1. **Streamlit App**
- Written in Python using Streamlit
- Launched from `app.py`
- Includes sections for About, Projects, Resume, and Contact

### 2. **Contact Form**
- Users can submit a message through a contact form
- On submission, the app sends an email (via FormSubmit or other service)
- Redirects to a hosted `thankyou.html` page

### 3. **Thank You Page**
- A custom HTML page (`thankyou.html`)
- Professionally styled with CSS
- Hosted using GitHub Pages
- Includes a “Back to Portfolio” button

---

## 🛠️ Setup Locally

```bash
# 1. Clone the repository
git clone https://github.com/MukeshDT/data-engineer-portfolio.git
cd data-engineer-portfolio

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install streamlit

# 4. Run the app locally
streamlit run app.py

---

## *De*
## 🌐 Setup Locally Deployment

#📌 1. Streamlit Cloud
Go to https://share.streamlit.io

Connect your GitHub repo

Choose app.py as the entry point

Deploy — a public URL is generated automatically

#📌 2. GitHub Pages for Thank You
Commit thankyou.html to the repo root

In GitHub settings:

Go to Pages

Set source: main branch → /root

Your page will be live at:
https://<your-username>.github.io/<repo-name>/thankyou.html
