# Simple Django Portfolio Example

This project is a basic portfolio website built using the Django web framework. It serves as a simple example demonstrating several core features of Django in a practical way.

## Features Demonstrated

This application showcases the following essential Django features:

1.  **MVT Architecture (Model-View-Template):**
    *   **Models (`portfolio/models.py`):** Defines the `Project` data structure stored in the database.
    *   **Views (`portfolio/views.py`):** Handles HTTP request logic (listing projects, processing contact form).
    *   **Templates (`templates/`):** Defines the HTML structure and presentation using Django Template Language (DTL).
2.  **ORM (Object-Relational Mapper):**
    *   Interacting with the database using Python objects (`Project.objects.all()`).
    *   **Migrations:** Managing database schema changes (`manage.py makemigrations`, `manage.py migrate`).
3.  **URL Routing (`portfolio_project/urls.py`, `portfolio/urls.py`):**
    *   Mapping URLs (web addresses) to specific view functions.
4.  **Templating Engine (DTL):**
    *   Dynamically generating HTML using tags (`{% %}`) and variables (`{{ }}`).
    *   **Template Inheritance:** Using a `base.html` template extended by other pages.
    *   **Template Filters:** Modifying variable display (e.g., `|truncatewords:20`).
5.  **Forms (`portfolio/forms.py`, `portfolio/views.py`, `templates/portfolio/contact.html`):**
    *   Defining form structure and validation rules (`ContactForm`).
    *   Rendering HTML forms in templates.
    *   Handling form submissions and validating data in views.
    *   **CSRF Protection:** Using `{% csrf_token %}` for security.
6.  **Admin Interface (`portfolio/admin.py`):**
    *   A built-in interface (`/admin/`) for managing site content (adding/editing/deleting `Project` entries).
7.  **Static File Handling (`settings.py`, `static/`, templates):**
    *   Managing CSS, JavaScript (via Bootstrap CDN in this case), and static images.
    *   Using the `{% static %}` template tag.
8.  **Media File Handling (`settings.py`, `models.py`, `media/`):**
    *   Handling user-uploaded files (project images via `ImageField`).
    *   Serving media files during development.
9.  **Settings (`portfolio_project/settings.py`):**
    *   Central project configuration (database, installed apps, templates, static/media files).

## Technology Stack

*   **Backend:** Python 3.x, Django
*   **Database:** SQLite (Default)
*   **Frontend:** HTML5, CSS3, Bootstrap 5 (via CDN)
*   **Image Handling:** Pillow
*   **Environment:** Virtual Environment (`venv`)

## Setup Instructions (Windows 11 / VS Code)

1.  **Prerequisites:**
    *   Python 3.x installed (ensure it's added to PATH).
    *   `pip` (Python package installer) installed.
    *   Visual Studio Code (or any code editor/IDE).
    *   Git (optional, if cloning from a repository).

2.  **Get the Code:**
    *   Clone this repository (if applicable) or download the project files.
    *   Open the project folder (`django_portfolio`) in VS Code.

3.  **Open VS Code Terminal:**
    *   Use `Terminal > New Terminal` (or `Ctrl+` `).

4.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    *(Your terminal prompt should now start with `(venv)`)*

5.  **Install Dependencies:**
    *   **(Optional but Recommended) Create `requirements.txt`:** If you haven't already, create a file listing dependencies:
        ```bash
        pip freeze > requirements.txt
        ```
    *   Install the required packages:
        ```bash
        pip install -r requirements.txt
        ```
        *Or, if you don't have `requirements.txt` yet:*
        ```bash
        pip install Django Pillow
        ```

6.  **Apply Database Migrations:**
    *   These commands create the database tables based on your models (`portfolio/models.py`).
    ```bash
    python manage.py makemigrations portfolio
    python manage.py migrate
    ```

7.  **Create a Superuser (Admin Account):**
    *   This account is used to access the Django admin interface.
    ```bash
    python manage.py createsuperuser
    ```
    *   Follow the prompts to set a username, email (optional), and password.

## Running the Application

1.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the Site:**
    *   Open your web browser and navigate to `http://127.0.0.1:8000/`

## Usage

*   **Homepage / Project List (`/`):** Displays the projects added via the admin panel. Shows images, titles, descriptions, and technologies.
*   **Admin Panel (`/admin/`):** Log in using the superuser credentials. Here you can:
    *   Add new projects (including uploading images).
    *   Edit existing projects.
    *   Delete projects.
*   **Contact Form (`/contact/`):** Allows users to send a message. The form includes basic validation. Upon successful submission, the data is printed to the console (in a real app, you would typically send an email or save it to the database) and the user is redirected to a success page.
