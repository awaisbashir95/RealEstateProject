# RealEstateDjango

A Django-based web application for managing and displaying real estate listings.

## Features

- Home, About, and Listings pages
- Featured property listings
- Django admin for managing listings and users
- PostgreSQL database support
- Responsive navigation with active state

## Requirements

- Python 3.11+
- Django 5.2+
- PostgreSQL
- psycopg2

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/RealEstateDjango.git
   cd RealEstateDjango
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   - Create a PostgreSQL database (e.g., `btredb`) using pgAdmin or psql.
   - Update `mysite/settings.py` with your database credentials.

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access):**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

8. **Access the app:**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```
RealEstateDjango/
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── listings/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── pages/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt
```

## License

This project is licensed under the MIT License.

---

**Feel free to contribute or open issues!**
