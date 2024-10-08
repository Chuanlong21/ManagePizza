# ManagePizza

A simple application to manage pizza adding.

## Requests
### 1. Manage Toppings
As a pizza store owner I should be able to manage toppings available for my pizza chefs.

It should allow me to see a list of available toppings
It should allow me to add a new topping
It should allow me to delete an existing topping
It should allow me to update an existing topping
It should not allow me to enter duplicate toppings

### 2. Manage Pizzas
As a pizza chef I should be able to create new pizza master pieces

It should allow me to see a list of existing pizzas and their toppings
It should allow me to create a new pizza and add toppings to it
It should allow me to delete an existing pizza
It should allow me to update an existing pizza
It should allow me to update toppings on an existing pizza
It should not allow me to enter duplicate pizzas

## Requirements

  - Python 3.10
  - PostgreSQL


## Installation

1. Git clone this repository
2. Run `pip install -r requirements.txt`
3.
```
If you are using PowerShell:
Run `$env:FLASK_APP = "app.py"` and `$env:FLASK_ENV = "development"`

CMD:
Run `set FLASK_APP=app.py` and `set FLASK_ENV=development`
```

## Configuration

Before running the application, you need to configure database connection in the `database.py`
```
def connect():
    return psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )

```

##  How to Run

### Run `flask run` to run locally

Then ManagePizza is available through [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Deployment on Google Cloud
[https://pizzastore-885119572301.us-central1.run.app/](https://pizzastore-885119572301.us-central1.run.app/)

##  How to Test

### 1: Add a New Topping
1. Navigate to http://127.0.0.1:5000/manage_toppings.
2. Enter a topping name in the "Topping Name" field (e.g., "Mushrooms").
3. Click the "Add" button.

### 2: Delete a Topping
1. Navigate to http://127.0.0.1:5000/manage_toppings.
2. Enter a existing topping name in the "Topping Name" field (e.g., "Mushrooms").
3. Click the "Delete" button.

### 3: Update a Topping
1. Navigate to http://127.0.0.1:5000/manage_toppings.
2. Enter the name of an existing topping and a new name in the "New Name for Update" field.
3. Click the "Delete" button.

### 4: Add a New Pizza
1. Navigate to http://127.0.0.1:5000/manage_pizzas.
2. Enter a pizza name (e.g., "Pepperoni Pizza").
3. Select toppings from the "Select Toppings" dropdown.
4. Click the "Add" button.

### 5: Update Pizza Toppings
1. Navigate to http://127.0.0.1:5000/manage_pizzas.
2. Enter a existing pizza name (e.g., "Pepperoni Pizza").
3. Update the toppings by selecting new toppings from the dropdown.
4. Click the "Update Toppings" button.

### 6: Delete a Pizza
1. Navigate to http://127.0.0.1:5000/manage_pizzas.
2. Enter a existing pizza name (e.g., "Pepperoni Pizza").
3. Click the "Delete" button.

### 7: Update a Pizza
1. Navigate to http://127.0.0.1:5000/manage_pizzas.
2. Enter the name of an existing pizza and a new name in the "New Name for Update" field.
3. Click the "Update" button.