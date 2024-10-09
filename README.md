# Superheroes_api


## Overview

The Superheroes API is a Flask application designed to track superheroes, their powers, and related customer reviews. This API provides endpoints for managing superheroes, their powers, and customer interactions through reviews.

## Models

### Customer

Represents a customer who can leave reviews for items.

- **Attributes:**
  - `id`: Unique identifier for each customer (Integer, Primary Key).
  - `name`: Name of the customer (String).

- **Relationships:**
  - `reviews`: A one-to-many relationship with the `Review` model.

### Item

Represents an item that customers can review.

- **Attributes:**
  - `id`: Unique identifier for each item (Integer, Primary Key).
  - `name`: Name of the item (String).
  - `price`: Price of the item (Float).

- **Relationships:**
  - `reviews`: A one-to-many relationship with the `Review` model.

### Review

Represents a customer's review for a specific item.

- **Attributes:**
  - `id`: Unique identifier for each review (Integer, Primary Key).
  - `comment`: The review comment (String).
  - `customer_id`: Foreign key referencing the `Customer` model (Integer).
  - `item_id`: Foreign key referencing the `Item` model (Integer).

- **Relationships:**
  - `customer`: A many-to-one relationship with the `Customer` model.
  - `item`: A many-to-one relationship with the `Item` model.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/Superheroes_api.git
   cd Superheroes_api

Create a virtual environment:
python3 -m venv venv

Activate the virtual environment:

On macOS/Linux:
source venv/bin/activate

On Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt
Set up the database:

Initialize the database:
flask db init

Create the migrations:
flask db migrate -m "Initial migration."

Apply the migrations:
flask db upgrade

Run the application:
flask run

API Endpoints
Customers
GET /customers - Retrieve all customers.
POST /customers - Create a new customer.
Items
GET /items - Retrieve all items.
POST /items - Create a new item.
Reviews
GET /reviews - Retrieve all reviews.
POST /reviews - Create a new review.

Contributing
Contributions are welcome! If you have suggestions for improvements, please fork the repository and create a pull request.