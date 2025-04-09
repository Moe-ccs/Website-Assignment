# Importing the necessary tools from Flask to build a web app and handle search requests
from flask import Flask, render_template, request, jsonify
# Starting the flask app
app = Flask(__name__)

# Below we have a list of the coffee shop locations around london with the minimum price of coffee and dessert
coffee_shops = {
    "Mayfair": {"coffee_price": 5, "dessert_price": 7},
    "Soho": {"coffee_price": 4.5, "dessert_price": 6.5},
    "Covent Garden": {"coffee_price": 4, "dessert_price": 6},
    "Shoreditch": {"coffee_price": 4.2, "dessert_price": 6.8},
    "Camden": {"coffee_price": 3.8, "dessert_price": 5.5},
    "Westminster": {"coffee_price": 5.5, "dessert_price": 7.5},
    "Chelsea": {"coffee_price": 5, "dessert_price": 6.8},
    "Kensington": {"coffee_price": 4.8, "dessert_price": 7},
    "Notting Hill": {"coffee_price": 4.5, "dessert_price": 6.5},
    "Greenwich": {"coffee_price": 4, "dessert_price": 5.8},
}
