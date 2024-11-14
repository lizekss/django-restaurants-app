# Restaurant Menu API

This project is a Django REST Framework-based API for managing restaurant menus, including categories, subcategories, and dishes. It allows users to create, update, and list menu items and their associated details.

## Features

- Manage menu categories and subcategories
- Create and update dishes with associated ingredients
- Filter and view menu items

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/restaurant-menu-api.git
   cd restaurant-menu-api
   ```
   
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
- **Menu Categories**
  - List all categories: [GET /menu-categories/](http://localhost:8000/menu-categories/)
  - Create a new category: [POST /menu-categories/create/](http://localhost:8000/menu-categories/create/)
  - Update an existing category: [PUT /menu-categories/update/<int:pk>/](http://localhost:8000/menu-categories/update/1/)
- **Subcategories**
  - List all subcategories: [GET /subcategories/](http://localhost:8000/subcategories/)
  - View a specific subcategory: [GET /subcategories/<int:subcategory_id>/](http://localhost:8000/subcategories/1/)
  - Create a new subcategory: [POST /subcategories/create/](http://localhost:8000/subcategories/create/)
  - Update an existing subcategory: [PUT /subcategories/update/<int:pk>/](http://localhost:8000/subcategories/update/1/)
- **Dishes**
  - Create a new dish: [POST /dishes/create/](http://localhost:8000/dishes/create/)
  - Update an existing dish: [PUT /dishes/update/<int:pk>/](http://localhost:8000/dishes/update/1/)

## Usage
Use tools like Postman or curl to interact with the API. You can also use the Django REST Framework's browsable API by navigating to the endpoints in your web browser.
