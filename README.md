<!-- [![Build Status](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi.svg?branch=api-v1)](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi) -->
![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Build Status](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi.svg?branch=api-v1)](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/fasrfoodfastapi/badge.svg?branch=api-v1)](https://coveralls.io/github/salma-nyagaka/fasrfoodfastapi?branch=api-v1)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/08730d5796eb49c8a545b128b7d7b80f)](https://www.codacy.com/app/salma-nyagaka/fasrfoodfastapi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=salma-nyagaka/fasrfoodfastapi&amp;utm_campaign=Badge_Grade)

# Fast Food Fast

Fast food fast is a fast food delivery application

# How it Works

- An admin creates food items
- A user can view available food items 
- A user chooses on a food item and makes an order
- An Admin can accept or reject the order request from a user
- A user gets notified on his/her order status
- Accepted orders are delivered to the user

# Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtua Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/salma-nyagaka/fasrfoodfast.git
```
# Create a virtual environment

    virtualenv venv --python=python3.6

# Activate virtual environment

    source venv/bin/activate

# Install required Dependencies

    pip install -r requirements.txt



# Endpoints Available

| Method | Endpoint                        | Description                           |
| ------ | ------------------------------- | ------------------------------------- |
| POST   | /api/v1/orders                  | Place an order                        |
| GET    | /api/v1/orders                  | Get all orders                        |
| PUT    | /api/v1/orders/<{id}>           | Update order status                   |
| GET    | /api/v1/orders/<{id}>           | Get a specific order                  |




# Author

Salma Nyagaka
