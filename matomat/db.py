#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongokit
import datetime
import config

config = config.configuration()
connection = mongokit.Connection(config["uri"])

@connection.register
class Beverage(mongokit.Document):
    __database__ = 'matomat'
    __collection__ = 'beverages'
    structure = {
            'name': unicode,
            'created': datetime.datetime,
            'price': float
    }
    required_fields = ['name', 'created', 'price']
    default_values = {
        'price': 1,
        'created': datetime.datetime.now
    }

@connection.register
class User(mongokit.Document):
    __database__ = 'matomat'
    __collection__ = 'users'
    structure = {
            'username': unicode,
            'password': unicode,
            "rights": list,
            "created": datetime.datetime,
            "active": bool,
            "rfid": unicode,
            "balance": float,
    }
    required_fields = ['username', 'created', 'password', 'rights', 'active', 'balance']
    default_values = {'created': datetime.datetime.now, 'balance': 0.0, 'active': True}


@connection.register
class Transaction(mongokit.Document):
    __database__ = 'matomat'
    __collection__ = 'transactions'
    structure = {
            "username": unicode,
            "beverage": unicode,
            "price": float,
            "created": datetime.datetime,
    }
    required_fields = ['username', 'beverage', 'price', 'created']
    default_values = {'created': datetime.datetime.now()}

