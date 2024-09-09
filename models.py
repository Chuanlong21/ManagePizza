
import psycopg2

from database import execute_query, fetch_query


# Toppings Management
def list_toppings():
    return fetch_query('SELECT * FROM Toppings')


def add_topping(name):
    try:
        print(f"Topping '{name}' added successfully.")
        execute_query('INSERT INTO Toppings (name) VALUES (%s)', (name,))
        print(f"Topping '{name}' added successfully.")
    except psycopg2.IntegrityError:
        print(f"Topping '{name}' already exists.")


def delete_topping(name):
    execute_query('DELETE FROM Toppings WHERE name = %s', (name,))
    print(f"Topping '{name}' deleted.")


def update_topping(old_name, new_name):
    try:
        execute_query('UPDATE Toppings SET name = %s WHERE name = %s', (new_name, old_name))
        print(f"Topping '{old_name}' updated to '{new_name}'.")
    except psycopg2.IntegrityError:
        print(f"Topping '{new_name}' already exists.")


# Pizza Management
def list_pizzas():
    return fetch_query('''
            SELECT Pizzas.name, STRING_AGG(Toppings.name, ', ') as toppings
            FROM Pizzas
            LEFT JOIN PizzaToppings ON Pizzas.id = PizzaToppings.pizza_id
            LEFT JOIN Toppings ON PizzaToppings.topping_id = Toppings.id
            GROUP BY Pizzas.name
        ''')


def add_pizza(name, toppings):
    try:
        execute_query('INSERT INTO Pizzas (name) VALUES (%s)', (name,))
        pizza_id = fetch_query('SELECT id FROM Pizzas WHERE name = %s', (name,))[0][0]
        for topping in toppings:
            topping_id = fetch_query('SELECT id FROM Toppings WHERE name = %s', (topping,))
            if topping_id:
                execute_query('INSERT INTO PizzaToppings (pizza_id, topping_id) VALUES (%s, %s)',
                              (pizza_id, topping_id[0][0]))
        print(f"Pizza '{name}' with toppings {toppings} added successfully.")
    except psycopg2.IntegrityError:
        print(f"Pizza '{name}' already exists.")


def delete_pizza(name):
    execute_query('DELETE FROM Pizzas WHERE name = %s', (name,))
    print(f"Pizza '{name}' deleted.")


def update_pizza(old_name, new_name):
    try:
        execute_query('UPDATE Pizzas SET name = %s WHERE name = %s', (new_name, old_name))
        print(f"Pizza '{old_name}' updated to '{new_name}'.")
    except psycopg2.IntegrityError:
        print(f"Pizza '{new_name}' already exists.")


def update_pizza_toppings(pizza_name, new_toppings):
    pizza_id = fetch_query('SELECT id FROM Pizzas WHERE name = %s', (pizza_name,))
    if not pizza_id:
        print(f"Pizza '{pizza_name}' not found.")
        return
    pizza_id = pizza_id[0][0]
    execute_query('DELETE FROM PizzaToppings WHERE pizza_id = %s', (pizza_id,))
    for topping in new_toppings:
        topping_id = fetch_query('SELECT id FROM Toppings WHERE name = %s', (topping,))
        if topping_id:
            execute_query('INSERT INTO PizzaToppings (pizza_id, topping_id) VALUES (%s, %s)',
                          (pizza_id, topping_id[0][0]))
    print(f"Pizza '{pizza_name}' toppings updated to {new_toppings}.")