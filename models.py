from database import execute_query, fetch_query


# Toppings Management
def list_toppings():
    return fetch_query('SELECT * FROM toppings')


def add_topping(name):
    print(name)
    execute_query('INSERT INTO toppings (name) VALUES (:name)', {'name': name})


def delete_topping(name):
    execute_query('DELETE FROM toppings WHERE name = :name', {'name': name})


def update_topping(old_name, new_name):
    execute_query('UPDATE toppings SET name = :new_name WHERE name = :old_name',
                  {'new_name': new_name, 'old_name': old_name})
    print(f"Topping '{old_name}' updated to '{new_name}'.")


# Pizza Management
def list_pizzas():
    return fetch_query('''
        SELECT Pizzas.name, STRING_AGG(toppings.name, ', ') as toppings
        FROM Pizzas
        LEFT JOIN pizzatoppings ON Pizzas.id = pizzatoppings.pizza_id
        LEFT JOIN toppings ON pizzatoppings.topping_id = toppings.id
        GROUP BY Pizzas.name
    ''')


def add_pizza(name, toppings):
    execute_query('INSERT INTO pizzas (name) VALUES (:name)', {'name': name})
    pizza_id = fetch_query('SELECT id FROM pizzas WHERE name = :name', {'name': name})[0][0]
    for topping in toppings:
        topping_id = fetch_query('SELECT id FROM toppings WHERE name = :name', {'name': topping})
        if topping_id:
            execute_query('INSERT INTO pizzatoppings (pizza_id, topping_id) VALUES (:pizza_id, :topping_id)',
                          {'pizza_id': pizza_id, 'topping_id': topping_id[0][0]})


def delete_pizza(name):
    execute_query('DELETE FROM pizzas WHERE name = :name', {'name': name})


def update_pizza(old_name, new_name):
    execute_query('UPDATE pizzas SET name = :new_name WHERE name = :old_name',
                  {'new_name': new_name, 'old_name': old_name})
    print(f"Pizza '{old_name}' updated to '{new_name}'.")


def update_pizza_toppings(pizza_name, new_toppings):
    pizza_id = fetch_query('SELECT id FROM pizzas WHERE name = :name', {'name': pizza_name})
    if not pizza_id:
        print(f"Pizza '{pizza_name}' not found.")
        return
    pizza_id = pizza_id[0][0]
    execute_query('DELETE FROM pizzatoppings WHERE pizza_id = :pizza_id', {'pizza_id': pizza_id})
    for topping in new_toppings:
        topping_id = fetch_query('SELECT id FROM toppings WHERE name = :name', {'name': topping})
        if topping_id:
            execute_query('INSERT INTO pizzatoppings (pizza_id, topping_id) VALUES (:pizza_id, :topping_id)',
                          {'pizza_id': pizza_id, 'topping_id': topping_id[0][0]})
