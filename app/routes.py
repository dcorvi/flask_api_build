from app import app

# jsonify works the same way that JSON.stringify does
# request is what allows us to take in parameters in the api call
from flask import render_template, jsonify, request

# don't confuse with request method above, requests is a library for calling api's, it is  specific to python, where request above is specific to flask
import requests


# index is going to call weather api and show information on front
@app.route('/')
@app.route('/index')
def index():
    API_KEY = app.config['WEATHER_API_KEY']
    # print(API_KEY)

    city = 'boston'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=imperial'

    #json() method convets string response into python dictionary
    response = requests.get(url).json()

    print(response)
    return render_template('index.html', response=response)


@app.route('/api/customers/', methods=['GET', 'POST'])
def apiCustomers():

    name = request.args.get('name')

    customers = [
            {
                'name': 'John',
                'age': 22
            },
            {
                'name': 'Alex',
                'age': 12
            },
            {
                'name': 'Annie',
                'age': 67
            },
            {
                'name': 'Jake',
                'age': 45
            },
            {
                'name': 'Bill',
                'age': 32
            },
        ]

    try:

        for customer in customers:
            if customer['name'] == name:
                return jsonify(customer)
    except:
        return jsonify({ 'Error 5000': 'Something went wrong '})

    return jsonify({ 'Error 304': 'No customer found' })
    # return jsonify({ '101': 'John Smith' })


# attempt
# @app.route('/api/customers/age', methods=['GET', 'POST'])
# def apiCustomersAge():
#     # accept an argument of min and max age, return all customers between those ages, make sure to use try and except to avoid errors
#
#     min = request.args.get('min')
#     max = request.args.get('max')
#
#     customers = [
#             {
#                 'name': 'John',
#                 'age': 22
#             },
#             {
#                 'name': 'Alex',
#                 'age': 12
#             },
#             {
#                 'name': 'Annie',
#                 'age': 67
#             },
#             {
#                 'name': 'Jake',
#                 'age': 45
#             },
#             {
#                 'name': 'Bill',
#                 'age': 32
#             },
#         ]
#     try:
#         results = []
#
#         for customer in customers:
#             if customer['age'] >= int(min) and customer['age'] <= int(max):
#                 results.append(customer)
#
#         return jsonify(results)
#     except:
#         return jsonify({'error': 'Incompatible parameter values'})

# solution
@app.route('/api/customers/age', methods=['GET', 'POST'])
def apiCustomersAge():
    # accept an argument of min and max age, return all customers between those ages, make sure to use try and except to avoid errors
    min = request.args.get('min')
    max = request.args.get('max')

    # print(request.args)

    # name is optional
    name = request.args.get('name')


    customers = [
        {
            'name': 'John',
            'age': 22
        },
        {
            'name': 'Alex',
            'age': 12
        },
        {
            'name': 'Annie',
            'age': 67
        },
        {
            'name': 'Jake',
            'age': 45
        },
        {
            'name': 'Bill',
            'age': 32
        },
    ]

    try:
        range = []

        for customer in customers:
            if customer['age'] < int(max) and customer['age'] > int(min):
                range.append(customer)

        if name:
            customers = []
            for customer in range:
                if customer['name'] == name:
                    customers.append(customer)
            return jsonify(customers)

        return jsonify(range)
    except:
        return jsonify({ 'error': 'Incompatible parameter values'})


    return jsonify({ 'error': 'Something went wrong' })
    # return jsonify({ 'complete this' })
    # return jsonify({ '101': 'John Smith' })

# attempt
# @app.route('/api/coords/', methods=['GET', 'POST'])
# def coords():
#     city = request.headers.get('city')
#
#     API_KEY = app.config['WEATHER_API_KEY']
#
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=imperial'
#
#     try:
#         # json() method converts string response into python dictionary
#         response = requests.get(url).json()
#         print(response)
#         return jsonify({
#             'city': response['name']
#             })
#     except:
#         return jsonify({ 'error': 'City does not exist' })


# solution
@app.route('/api/coords', methods=['GET', 'POST'])
def coords():
    city = request.headers.get('city')

    API_KEY = app.config['WEATHER_API_KEY']

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=imperial'

    try:
        # json() method converts string response into python dictionary
        response = requests.get(url).json()
        print(response)
        return jsonify({
            'city': response['name'],
            'longitude': response['coord']['lon'],
            'latitude': response['coord']['lat']
        })
    except:
        return jsonify({ 'error': 'City does not exist' })
