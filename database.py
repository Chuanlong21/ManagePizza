
import os
import psycopg2


DATABASE_URL = os.environ.get('DATABASE_URL')


def connect():
    return psycopg2.connect(DATABASE_URL, sslmode='require')


def execute_query(query, params=()):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()


def fetch_query(query, params=()):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result


def create_tables():
    execute_query('''
        CREATE TABLE IF NOT EXISTS Toppings (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL
        )
    ''')
    execute_query('''
        CREATE TABLE IF NOT EXISTS Pizzas (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL
        )
    ''')
    execute_query('''
        CREATE TABLE IF NOT EXISTS PizzaToppings (
            pizza_id INTEGER,
            topping_id INTEGER,
            FOREIGN KEY (pizza_id) REFERENCES Pizzas(id),
            FOREIGN KEY (topping_id) REFERENCES Toppings(id),
            UNIQUE (pizza_id, topping_id)
        )
    ''')
