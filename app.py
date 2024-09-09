from flask import Flask, render_template, request, redirect, url_for, flash
from models import list_toppings, add_topping, delete_topping, update_topping
from models import list_pizzas, add_pizza, delete_pizza, update_pizza, update_pizza_toppings
from database import create_tables

create_tables()

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/manage_toppings', methods=['GET', 'POST'])
def manage_toppings():
    if request.method == 'POST':
        action = request.form.get('action')
        name = request.form.get('name')
        new_name = request.form.get('new_name', '')

        if action == 'add':
            add_topping(name)
        elif action == 'delete':
            delete_topping(name)
        elif action == 'update':
            update_topping(name, new_name)

        flash(f"Topping action '{action}' executed.")
        return redirect(url_for('manage_toppings'))

    toppings = list_toppings()
    return render_template('manage_toppings.html', toppings=toppings)


@app.route('/manage_pizzas', methods=['GET', 'POST'])
def manage_pizzas():
    if request.method == 'POST':
        action = request.form.get('action')
        name = request.form.get('name')
        new_name = request.form.get('new_name', '')
        toppings = request.form.getlist('toppings')

        if action == 'add':
            add_pizza(name, toppings)
        elif action == 'delete':
            delete_pizza(name)
        elif action == 'update':
            update_pizza(name, new_name)
        elif action == 'update_toppings':
            update_pizza_toppings(name, toppings)

        flash(f"Pizza action '{action}' executed.")
        return redirect(url_for('manage_pizzas'))

    pizzas = list_pizzas()
    toppings = list_toppings()
    return render_template('manage_pizzas.html', pizzas=pizzas, toppings=toppings)


if __name__ == '__main__':
    app.run(debug=True)
