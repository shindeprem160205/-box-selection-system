# AI-Assisted Box Selection System

A Django REST Framework application that recommends the most suitable shipping box for an order based on product dimensions, product weight, box dimensions, box weight capacity, and box cost.

## Features

- Product management
- Shipping box management
- Order and order-item management
- Box recommendation API
- Dimension-based box validation
- Product rotation support
- Weight-capacity validation
- Cheapest suitable box selection
- Input validation
- Django Admin interface
- Automated unit and API tests

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Django Test Framework

## Project Structure

```text
box-selection-system/
├── boxes/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── services.py
│   └── tests.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── requirements.txt
├── .gitignore
├── README.md
├── AI_USAGE.md
├── TEST_OUTPUT.md
└── manage.py

Data Models
Product
Stores product information:
- Name
- Length
- Width
- Height
- Weight
Dimensions are stored in centimeters and weight is stored in kilograms.
Box
Stores shipping box information:
- Name
- Internal length
- Internal width
- Internal height
- Maximum weight
- Cost
Order
Represents a customer order.
OrderItem
Connects an order with a product and stores the quantity ordered.
Box Recommendation Logic
The recommendation service follows these steps:
1. Calculate the total weight of the order.
2. Check whether the total weight is within the box's maximum weight capacity.
3. Check whether each product can fit within the box dimensions.
4. Product rotation is supported by comparing sorted dimensions.
5. Collect all suitable boxes.
6. Select the suitable box with the lowest cost.
7. Return no recommendation if no suitable box exists.
Recommendation Endpoint
POST /api/orders/<order_id>/recommend-box/

Example response:
{
    "order_id": 1,
    "recommended_box": {
        "id": 1,
        "name": "Small Box",
        "cost": "50.00"
    }
}

If no suitable box exists:
{
    "detail": "No suitable box found for this order."
}

API Endpoints
Products
GET  /api/products/
POST /api/products/

Boxes
GET  /api/boxes/
POST /api/boxes/

Orders
GET  /api/orders/
POST /api/orders/

Box Recommendation
POST /api/orders/<order_id>/recommend-box/

Setup Instructions
1. Clone the repository
git clone <repository-url>
cd box-selection-system

2. Create a virtual environment
python -m venv .venv

3. Activate the virtual environment
Windows PowerShell:
.venv\Scripts\Activate.ps1

4. Install dependencies
pip install -r requirements.txt

5. Apply migrations
python manage.py migrate

6. Run the development server
python manage.py runserver

The application will be available at:
http://127.0.0.1:8000/

Admin Panel
Create an administrator:
python manage.py createsuperuser

Then open:
http://127.0.0.1:8000/admin/

The admin panel provides access to:
- Products
- Boxes
- Orders
- Order items
Running Tests
Run the complete test suite:
python manage.py test

The tests cover:
- Total order weight calculation
- Product dimension checking
- Product rotation
- Cheapest suitable box selection
- Weight capacity rejection
- Dimension rejection
- No suitable box scenario
- Recommendation API
- Invalid order handling
- Product validation
- Box validation
- Order quantity validation
The final test execution output is available in:
TEST_OUTPUT.md

## What Did I Learn?

The main objective of the project was to find the right box for the products because it was a kind of recommendation system where boxes were chosen based on the size of the products. For this we used API testing, DRF and Django.

While working on this project I learned how to create DRF APIs as someone who was just starting out. During the task I also learned how to make and design database models by thinking about how our data should be organized and then putting that organization into my project.

I also learned how to handle connections, between orders order items and products. The main thing I learned was the use of serializers. I also got better at organizing my project. Learned how to keep that organization even after several mistakes, wrong files and changes. I learned how to keep my project organized, clear and easy to read.

## Test Cases

The project includes automated test cases covering:

- Total order weight calculation
- Product dimension validation
- Box weight capacity validation
- Cheapest suitable box selection
- Product rotation
- No suitable box available
- Recommendation API success response
- Recommendation API when no box fits
- Invalid order ID
- Zero quantity validation
- Product input validation
- Box input validation

## Assumptions & Limitations

- Product dimensions are compared with box dimensions after sorting, so product rotation is supported.
- The current implementation checks whether each individual product fits inside the box and whether the total order weight is within the box capacity.
- It does not implement a full 3D packing algorithm for physically arranging multiple different products inside one box.
- SQLite is used for simplicity for this assignment.
