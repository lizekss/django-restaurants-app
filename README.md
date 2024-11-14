# Restaurant Menu API

This project is a Django REST Framework-based API for managing restaurant menus, including categories, subcategories, and dishes. It allows users to create, update, and list menu items and their associated details.

## Features

- Manage menu categories and subcategories
- Create and update dishes with associated ingredients
- Filter and view menu items

## Installation

1. **Clone the repository:**

2. **Install the dependencies:**
   
```bash
   pip install -r requirements.txt
```

5. **Run the development server:**
   
```bash
   python manage.py runserver
```
   
## Accessing the Application

### Admin Authentication
```
username: lizi
password: 1234
```

The following endpoints are available for interacting with the API:

### Menu app: `/menu`
- **Menu Categories**
  - List all categories: [GET /menu-categories/](http://localhost:8000/menu/menu-categories/)
  - Create a new category: [POST /menu-categories/create/](http://localhost:8000/menu/menu-categories/create/)
  - Update an existing category: [PUT /menu-categories/update/<int:pk>/](http://localhost:8000/menu/menu-categories/update/1/)
- **Subcategories**
  - List all subcategories: [GET /subcategories/](http://localhost:8000/menu/subcategories/)
  - View a specific subcategory: [GET /subcategories/<int:subcategory_id>/](http://localhost:8000/menu/subcategories/1/)
  - Create a new subcategory: [POST /subcategories/create/](http://localhost:8000/menu/subcategories/create/)
  - Update an existing subcategory: [PUT /subcategories/update/<int:pk>/](http://localhost:8000/menu/subcategories/update/1/)
- **Dishes**
  - Create a new dish: [POST /dishes/create/](http://localhost:8000/menu/dishes/create/)
  - Update an existing dish: [PUT /dishes/update/<int:pk>/](http://localhost:8000/menu/dishes/update/1/)

## Usage
Use tools like Postman or curl to interact with the API. You can also use the Django REST Framework's browsable API by navigating to the endpoints in your web browser.
