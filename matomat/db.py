#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mongokit
import datetime


class db:
    uri = None
    connection = None

    def __init__(self, mongodb_uri):
        self.uri = mongodb_uri
        self.connection = mongokit.Connection(self.uri)
        self.connection.register([Beverage, User, Transaction])


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

