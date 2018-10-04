![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Build Status](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi.svg?branch=api-v2)](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/fasrfoodfastapi/badge.svg?branch=api-v2)](https://coveralls.io/github/salma-nyagaka/fasrfoodfastapi?branch=api-v2)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/08730d5796eb49c8a545b128b7d7b80f)](https://www.codacy.com/app/salma-nyagaka/fasrfoodfastapi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=salma-nyagaka/fasrfoodfastapi&amp;utm_campaign=Badge_Grade)

## Fast Food Fast

Fast food fast is a fast food delivery application

# How it Works
- User can signin/signout from the app. 
- User can an order for food.
- User can get a history list of orders.
- Admin can get all user orders
- Admin can get a specific order.
- Admin can uppdate the status of an order. 
- Admin and user can get the menu.
- Add food option to the menu.


## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

## Installation and Setup

Clone the repository below

```
git clone -b api-v2 https://github.com/salma-nyagaka/fasrfoodfast.git
```
# Create a virtual environment

    -virtualenv venv --python=python3.6


# Create a .env file

    $ touch .env

    Set the environment variables

    -export FLASK_APP="run.py"
    -export APP_SETTINGS="development"
    -export FLASK_DEBUG=1
    -export JWT_SECRET_KEY="aduscaecawserydtvyubiun1234567******sfc"
    -export DATABASE_URL="dbname='fast_food_db' host='127.0.0.1' port='5432' user='fast_food_user' password='salma'"
    -export DATABASE_TEST_URL="dbname='fast_food_test_db' host='127.0.0.1' port='5432' user='fast_food_user' password='salma'"



# Install required Dependencies

    pip install -r requirements.txt

# Run thee .env file

    source .env

# Endpoints Available

| Method | Endpoint                        | Description                           | 
| ------ | ------------------------------- | ------------------------------------- | 
| POST   | /api/v2/auth/signup             | User sign up                          |
| POST   | /api/v2/auth/login              | User login                            | 
| POST   | /api/v2/users/orders/<{id}>     | User places an order                  | 
| GET   | /api/v2/users/orders             | User gets the order history           | 
| GET   | /api/v2/orders                   | Admin gets all the orders             | 
| GET   | /api/v2/orders                   | Admin gets all the orders             | 
| GET   | /api/v2/orders/<{id}>             | Admin gets specific order            | 
| PUT   | /api/v2/orders/<{id}>            | Admin updates order status            | 
| GET   | /api/v2/menu                     | Admin gets the available menu         | 
| GET   | /api/v2/menu                     | Admin adds a meal option to the menu  | 

