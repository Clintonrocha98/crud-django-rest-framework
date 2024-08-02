
---

<h1 align="center" style="font-weight: bold;">Toy API 🎮</h1>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#started">Getting Started</a> • 
 <a href="#routes">API Endpoints</a> •
 <a href="#testing">Tests</a> 
</p>

<p align="center">
    <b>An API for managing a collection of toys, including operations for creating, reading, updating, and deleting toys.</b>
</p>

<h2 id="tech">💻 Technologies</h2>

- Python
- Django
- Django REST Framework
- SQLite

<h2 id="started">🚀 Getting started</h2>

<h3>Prerequisites</h3>

Make sure you have the following installed:

- [Python 3.12.3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

<h3>Cloning</h3>

Clone the repository to your local machine:

```bash
git clone git@github.com:Clintonrocha98/crud-django-rest-framework.git
```

<h3>Installing Dependencies</h3>

Navigate to the project directory and install the necessary dependencies:

```bash
cd restful01

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

<h3>Applying Migrations</h3>

Apply database migrations to set up the SQLite database:

```bash
python manage.py migrate
```

<h3>Starting the Server</h3>

Start the Django development server:

```bash
python manage.py runserver
```

<h2 id="routes">📍 API Endpoints</h2>

Below are the main routes of the API and their expected request/response details.

| route                    | description                                |
|---------------------------|--------------------------------------------|
| <kbd>GET /toys/</kbd>     | Retrieves a list of all toys               |
| <kbd>POST /toys/</kbd>    | Creates a new toy                          |
| <kbd>GET /toys/{id}/</kbd>| Retrieves details of a specific toy by ID  |
| <kbd>PATCH /toys/{id}/</kbd>| Partially updates a toy by ID             |
| <kbd>DELETE /toys/{id}/</kbd>| Deletes a toy by ID                      |

<h3 id="get-toys">GET /toys/</h3>

**RESPONSE**
```json
[
    {
        "id": 1,
        "name": "Toy 1",
        "description": "Description 1",
        "price": 100.0,
        "category": "Category 1",
        "was_included_in_home": false
    },
    {
        "id": 2,
        "name": "Toy 2",
        "description": "Description 2",
        "price": 150.0,
        "category": "Category 2",
        "was_included_in_home": true
    }
]
```

<h3 id="post-toys">POST /toys/</h3>

**REQUEST**
```json
{
    "name": "Toy 3",
    "description": "Description 3",
    "price": 120.0,
    "category": "Category 3",
    "was_included_in_home": false
}
```

**RESPONSE**
```json
{
    "id": 3,
    "name": "Toy 3",
    "description": "Description 3",
    "price": 120.0,
    "category": "Category 3",
    "was_included_in_home": false
}
```

<h3 id="patch-toys">PATCH /toys/{id}/</h3>

**REQUEST**
```json
{
    "price": 130.0
}
```

**RESPONSE**
```json
{
    "id": 3,
    "name": "Toy 3",
    "description": "Description 3",
    "price": 130.0,
    "category": "Category 3",
    "was_included_in_home": false
}
```

<h3 id="delete-toys">DELETE /toys/{id}/</h3>

**RESPONSE**
```json
{
}
```
<h2 id="testing">🧪 Running Tests</h2>
To ensure that everything is working correctly, you can run the tests included in this project.

<h3>Running the Tests</h3>

To run the tests, use the following command:

```bash
python manage.py test
```

This command will automatically discover and execute all tests in the project, providing you with a summary of the results.