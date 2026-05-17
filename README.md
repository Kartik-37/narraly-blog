<div align="center">

<picture >
  <source media="(prefers-color-scheme: dark)" srcset="home/static/image/nav/Logo_White.png">
  <source media="(prefers-color-scheme: light)" srcset="home/static/image/nav/logom.png">
  <img alt="Narraly Logo" src="home/static/image/nav/logom.png" width="500">
</picture>

# Narraly

### *The home for writers & readers*

> **Create, collaborate, and share your story.**
> A full-stack blogging platform built with Django — deployed live on Render.

<br/>

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-narraly--blog.onrender.com-6C63FF?style=for-the-badge&logoColor=white)](https://narraly-blog.onrender.com)
&nbsp;
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
&nbsp;
[![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
&nbsp;
[![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
&nbsp;
[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red?style=for-the-badge)](https://github.com/Kartik-37/narraly-blog#-copyright--license)

<br/>

---

### 🌐 [View Live → narraly-blog.onrender.com](https://narraly-blog.onrender.com)

---

</div>

<br/>

## 🗂️ Table of Contents

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Deployment](#-deployment)
- [What Writers Say](#-what-writers-say)
- [Contact](#-contact)
- [Copyright](#-copyright--license)

---

## 📖 About

**Narraly** is a production-ready, full-stack blogging platform designed for the modern creator. Built entirely with **Python & Django**, it offers writers a clean, distraction-free space to publish stories — and readers a community-driven feed to discover content they love.

Unlike a basic blog app, Narraly is built like a real product: with user authentication, a follow system, real-time notifications, bookmarks, and a community feed — all deployed live on the web.

> *"Effortlessly build blogs, product guides, and more — fast, easy, and powerful."*

---

## ✨ Features

### 🖊️ Writing & Publishing
- **Rich Text Editor** — Clean, distraction-free editor with rich formatting, headings, and image support
- **Instant Publishing** — Go from draft to live blog in seconds
- **Personal Profile** — Every writer gets their own author profile

### 🌍 Community & Discovery
- **Community Feed** — Browse stories from all writers on the platform
- **Follow System** — Follow writers you love and build your personal reading network
- **Trending Content** — Discover what the community is reading most

### 🔖 Reader Experience
- **Bookmarks** — Save any blog to your personal reading list, synced across sessions
- **Likes & Comments** — Engage with stories and leave feedback
- **Real-Time Notifications** — Instant alerts for likes, comments, and new followers

### 🔐 Authentication & Security
- **User Registration & Login** — Secure account system
- **Session Management** — Protected routes and authenticated views
- **Django Security** — CSRF protection, secure settings for production

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Python 3, Django | Core application logic, ORM, routing |
| **Frontend** | HTML5, CSS3, JavaScript | Templating, styling, interactivity |
| **Database** | SQLite | Data persistence |
| **Deployment** | Render | Cloud hosting, CI/CD |
| **Static Files** | Django WhiteNoise | Serving CSS, JS, images in production |
| **Media Storage** | Django Media | Storing user-uploaded images |

</div>

---

## 📁 Project Structure

```
narraly-blog/
│
├── 📂 home/                # Core Django app
│   ├── models.py           #   Database models (Post, User, Bookmark, etc.)
│   ├── views.py            #   All page views and logic
│   ├── urls.py             #   URL routing
│   └── templates/          #   HTML templates
│
├── 📂 proj2/               # Django project config
│   ├── settings.py         #   App settings (dev & production)
│   └── urls.py             #   Root URL configuration
│
├── 📂 media/               # User-uploaded images and files
│
├── manage.py               # Django management entry point
├── requirements.txt        # Python package dependencies
├── build.sh                # Render build script
├── render.yaml             # Render service configuration
├── runtime.txt             # Python version specification
└── db.sqlite3              # SQLite database
```

---

## 🚀 Getting Started

> ⚠️ **This project is shared for portfolio and demonstration only.**
> Copying or reusing this code is strictly prohibited. See [Copyright](#-copyright--license).

### Prerequisites

- Python 3.x installed
- pip package manager

### Run Locally

```bash
# Step 1 — Clone the repository
git clone https://github.com/Kartik-37/narraly-blog.git
cd narraly-blog

# Step 2 — Install all dependencies
pip install -r requirements.txt

# Step 3 — Apply database migrations
python manage.py migrate

# Step 4 — Start the development server
python manage.py runserver
```

Then open **http://127.0.0.1:8000** in your browser.

---

## 🌐 Deployment

Narraly is deployed on **[Render](https://render.com)** — a modern cloud platform for web applications.

| File | Purpose |
|------|---------|
| `render.yaml` | Defines the Render web service configuration |
| `build.sh` | Runs on each deploy: installs packages, collects static files, migrates DB |
| `runtime.txt` | Pins the Python version for the Render environment |

The app is live at: **[https://narraly-blog.onrender.com](https://narraly-blog.onrender.com)**

---

## 💬 What Writers Say

> *"Narraly made it so easy to start writing. The editor is clean, the community is supportive, and I got my first readers within days."*
>
> — **Mahesh K.**, Tech Blogger

---

> *"I love how I can follow people whose writing I enjoy. It feels like a real community, not just a publishing tool."*
>
> — **Parth R.**, Food Writer

---

> *"The bookmark feature is a game changer. I can save blogs and come back to them whenever I want."*
>
> — **KD DRK**, Creative Writer

---

## 📬 Contact

<div align="center">

**Kartik** — Full-Stack Developer & Designer

[![GitHub](https://img.shields.io/badge/GitHub-Kartik--37-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Kartik-37)
&nbsp;
[![Live Project](https://img.shields.io/badge/Project-Narraly-6C63FF?style=for-the-badge&logo=render&logoColor=white)](https://narraly-blog.onrender.com)

</div>

---

## 🔒 Copyright & License

<div align="center">

**© 2025 Kartik. All Rights Reserved.**

</div>

This repository is **publicly visible for portfolio and evaluation purposes only.**
The source code is the exclusive intellectual property of the author.

### ❌ The following are strictly NOT permitted:

| Action | Status |
|--------|--------|
| Copying or reproducing any part of this code | ❌ Prohibited |
| Using this code in your own projects | ❌ Prohibited |
| Redistributing or sublicensing this code | ❌ Prohibited |
| Modifying and presenting as your own work | ❌ Prohibited |
| Commercial use of any kind | ❌ Prohibited |

### ✅ What is allowed:

- Viewing the code for learning or evaluation purposes
- Sharing the **live demo link** to showcase the project

> For any permissions or collaboration inquiries, contact via GitHub: [@Kartik-37](https://github.com/Kartik-37)

---

<div align="center">

**Built with ❤️ by [Kartik](https://github.com/Kartik-37)**

*Narraly — Where stories come to life.*

</div>
