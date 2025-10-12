# 🛫 Django Airfields

**Django Airfields** is a reusable Django app that provides an extendable model and admin interface for managing airport and airfield data — such as ICAO codes, names, locations, and related information.

This package is designed to be modular and easily integrated into other aviation-related Django projects.

---

## 🚀 Features

- Django model for managing airfields (ICAO, IATA, name, city, country, etc.)
- Admin interface for easy data management
- Clean separation for packaging and reuse
- Compatible with Django 3.2+

---

## 🧰 Installation

```bash
pip install django-airfields
```
---

## ⚙️ Setup
Add **airfields** to your **INSTALLED_APPS** in settings.py:

```python
INSTALLED_APPS = [
    ...
    'airfields',
]
```

Run migrations:
```bash
python manage.py makemigrations airfields
python manage.py migrate airfields
```

## 🧩 Usage Example

You can now use the Airfield model anywhere in your Django project:
```python
from airfields.models import Airfield

# create an airfield
Airfield.objects.create(
    icao="GABS",
    iata="BKO",
    name="Bamako Senou International Airport",
    city="Bamako",
    country="Mali"
)

# list all airfields
for af in Airfield.objects.all():
    print(af.name)
```