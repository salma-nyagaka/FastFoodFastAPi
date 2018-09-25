![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Build Status](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi.svg?branch=api-v1)](https://travis-ci.org/salma-nyagaka/fasrfoodfastapi)
[![Coverage Status](https://coveralls.io/repos/github/salma-nyagaka/fasrfoodfastapi/badge.svg?branch=api-v1)](https://coveralls.io/github/salma-nyagaka/fasrfoodfastapi?branch=api-v1)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/08730d5796eb49c8a545b128b7d7b80f)](https://www.codacy.com/app/salma-nyagaka/fasrfoodfastapi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=salma-nyagaka/fasrfoodfastapi&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/a236552c6eda78af4c69/maintainability)](https://codeclimate.com/github/salma-nyagaka/fasrfoodfast/maintainability)

# Fast Food Fast

Fast food fast is a fast food delivery application

# How it Works

- An admin views orders
- A admin places an order
- An admin can delete an order
- An admin can accept an order
- An admin can mark order as completed
- An admin can mark order as declined

# Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and Setup

Clone the repository below

```
git clone -b api-v1 https://github.com/salma-nyagaka/fasrfoodfast.git
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
| GET    | /api/v1/orders/<{id}>           | Get a specific order                  |
| PUT    | /api/v1/accept/orders/<{id}>    | Accept an order                       |
| PUT    | /api/v1/complete/orders/<{id}>  | Complete an order                     |
| PUT    | /api/v1/decline/orders/<{id}>   | Decline an order                      |
| DELETE | /api/v1/orders/<{id}>           | Delete a specific order               |
| DELETE | /api/v1/orders/<{id}>           | Delete a specific order               |
