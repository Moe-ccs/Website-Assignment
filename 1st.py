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
# The code below shows the main page when someone visits the website
@app.route('/')
def home():
    return render_template("1st.html")  # Make sure your HTML file is named correctly
# The code below is responsible to handle the search requests from the user
@app.route('/search', methods=['POST'])
def search():
    # Geting the location entered by the user
    location = request.json.get("location")
# Checking if we have prices for the location entered
    if location in coffee_shops:
        coffee_price = coffee_shops[location]["coffee_price"]
        dessert_price = coffee_shops[location]["dessert_price"]
        total_price = coffee_price + dessert_price
        # Sending back a total price message for the user
        return jsonify({"success": True, "message": f"In {location}, coffee and dessert cost approximately £{total_price:.2f}."})
    else:
        # Outputs a message telling the user that the location they entered is not available
        return jsonify({"success": False, "message": "Not available in this location. Try another area."})
