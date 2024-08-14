# Django URL Shortener

## Overview

Welcome to the Django URL Shortener project! This web application, built by Django, allows users to shorten long URLs, making them easier to share and manage. 

## Features

- **URL Shortening**: Convert long URLs into shorter, more manageable links.
- **URL Redirection**: Redirect users from short URLs to the original long URLs.


## Getting Started
1. Clone the Repository:
```bash
git clone https://github.com/tahsinj/URLShortener.git
```
2. Create a Virtual Environment
```bash
python -m venv .venv
.venv/Scripts/activate  # On MacOS/Linux use `source venv/bin/activate`
```
3. Install Dependencies:
```bash
pip install requirements.txt
```
4. Apply Migrations:
```bash
python manage.py migrate
```
5. Run the Development Server:
```bash
python manage.py runserver
```
6. **Access the Application:**

   Open your browser and navigate to `http://127.0.0.1:8000`.

