# Django URL Shortener

## Overview

This URL Shortener project is built using the Django framework to help simplify lengthy URLs into shorter more manageable URLs.

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

   Open your browser and navigate to `http://127.0.0.1:8000` or `http://localhost:8000`.

