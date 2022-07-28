# Course Catalog

Django full-stack site hosting our course catalog.

The site's intended use is for staff to manage the catalog.

Users can sign up / log in to have full CRUD functionality.

### How to run locally

- Create a virtual environment
- Install dependencies (requirements.txt)
- Run: python manage.py runserver

---

### Technical Features

- Custom CSS
- Gunicorn server
- Custom user model
- Deployed on Heroku
- Environment variables
- Full CRUD funtionality
- Cloud Postgres database

### Design decisions

- Uses Django generic views
- Uses Django generic forms

### Areas for improvement

- Use custom user sign up and log in forms
- Use is owner or read only permissions
- Add email verification