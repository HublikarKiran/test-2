# Student System Django Project

Project name: `studentsystem`

Apps:

- `student`
- `faculty`
- `parent`
- `admin`

This is a beginner to moderate level Django project. Admin creates all users and role profiles. Students, parents, and faculty only login using credentials provided by admin.

Each app has its own `views.py` and `urls.py`. The main `studentsystem/urls.py` only connects these app URLs together.

## Main URLs

- `http://127.0.0.1:8000/` - default landing page
- `http://127.0.0.1:8000/home/` - redirects to landing page
- `http://127.0.0.1:8000/login/` - login page
- `http://127.0.0.1:8000/dashboard/` - redirects user based on role
- `http://127.0.0.1:8000/django-admin/` - Django admin panel

## App URL Files

- `admin/urls.py` - landing page, login, logout, role dashboard redirection, admin dashboard
- `student/urls.py` - student dashboard
- `faculty/urls.py` - faculty dashboard
- `parent/urls.py` - parent dashboard

## How Login Redirection Works

- Superuser or admin profile -> admin dashboard
- Student profile -> student dashboard
- Faculty profile -> faculty dashboard
- Parent profile -> parent dashboard

## Run With SQLite3

SQLite is already configured in `studentsystem/settings.py`.

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If your default `python` does not have Django installed, install Django for that Python:

```bash
python -m pip install Django==5.2.6
```

## Creating Users

1. Login to `http://127.0.0.1:8000/django-admin/` using the superuser.
2. Create a normal Django `User`.
3. Create exactly one role profile for that user:
   - `StudentProfile`
   - `FacultyProfile`
   - `ParentProfile`
   - `AdminProfile`
4. Give the username and password to the user.

There is no public registration page in this project.

## MySQL Database Creation Query

Open MySQL and run:

```sql
CREATE DATABASE studentsystem_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER 'studentsystem_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON studentsystem_db.* TO 'studentsystem_user'@'localhost';
FLUSH PRIVILEGES;
```

## MySQL Settings Code

Replace the current `DATABASES` block in `studentsystem/settings.py` with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studentsystem_db',
        'USER': 'studentsystem_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

Then install the MySQL driver:

```bash
pip install mysqlclient
```

After changing from SQLite3 to MySQL, run:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## What Changes When Shifting SQLite3 To MySQL

- Change only the `DATABASES` setting in `studentsystem/settings.py`.
- Install a MySQL driver such as `mysqlclient`.
- Create the MySQL database before running migrations.
- Run migrations again because MySQL starts with empty tables.
- Create a new superuser for MySQL unless you migrate old SQLite data separately.
- SQLite stores data in `db.sqlite3`; MySQL stores data in the MySQL server.

## Important Beginner Notes

- The app folder is named `admin` because that was requested, but its internal Django app label is `system_admin` to avoid clashing with Django's built-in admin app.
- The real Django admin panel URL is `/django-admin/`, not `/admin/`.
- Marks and attendance are entered by admin from the Django admin panel for now.
- This project is intentionally simple and not fully dynamic yet.
