# flask project
from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'GET':
        return jsonify({"message": "Welcome to Currency Converter API!"})
     
    try:
        data = request.get_json()

        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        # If parameters are missing, return an error
        if not all([source_currency, amount, target_currency]):
            return jsonify({"fulfillmentText": "Invalid input. Please provide currency details!"}), 400
        
        value = getCurrAPI(source_currency, target_currency, amount)

        return jsonify({"fulfillmentText": f"{amount} {source_currency} is {value['totalValue']} {target_currency}"})
    
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"fulfillmentText": "An error occurred while processing your request."}), 500


# @app.route('/api', methods=['GET'])
def getCurrAPI(source_currency, target_currency, amount):

    # api to get the currency rate
    url = f'https://api.exchangerate-api.com/v4/latest/{source_currency}'
    response = requests.get(url)
    json = response.json() 
    return {
        'currCode' : json['rates'][target_currency], 
        'totalValue' : json['rates'][target_currency] * amount
        }


if __name__ == "__main__":
    app.run(debug=True)
