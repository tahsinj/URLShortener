# Django URL Shortener

## Overview

Welcome to the Django URL Shortener project! This web application, built by Django, allows users to shorten long URLs, making them easier to share and manage. 

## Features

- **URL Shortening**: Convert long URLs into shorter, more manageable links.
- **URL Redirection**: Redirect users from short URLs to the original long URLs.

## Project Structure
URLShortener/
├── manage.py
├── urlshort/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── shortener/
│   │       ├── index.html
│   │       ├── shorten.html
│   │       ├── manage.html
│   └── static/
│       └── shortener/
│           ├── css/
│           ├── js/
├── URLShortener/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── requirements.txt
