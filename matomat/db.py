#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongokit import *
import datetime
import matomat.config

config = matomat.config.configuration()
connection = Connection(config["uri"])

@connection.register
class Beverage(Document):
    __database__ = 'matomat'
    __collection__ = 'beverages'
    structure = {
            'name':unicode,
            'created':datetime.datetime,
            'price':float
    }
    required_fields = ['name','created', 'price']
    default_values = {'price':1, 'created':datetime.datetime.now}

@connection.register
class User(Document):
    __database__ = 'matomat'
    __collection__ = 'users'
    structure = {
            'username':unicode,
            'password':unicode,
            "roles":list,  # ["adduser", "otherrole"]
            "created":datetime.datetime,
            "active":bool,
            "rfid":unicode,
            "balance":float,
    }
    required_fields = ['username','created', 'password', 'roles', 'active', 'balance']
    default_values = {'price':1, 'created':datetime.datetime.now, 'balance':0, 'active':True}


@connection.register
class Transaction(Document):
    __database__ = 'matomat'
    __collection__ = 'transactions'
    structure = {
            "username":unicode,
            "beverage":unicode,
            "price":float,
            "created": datetime.datetime,
    }
    required_fields = ['username', 'beverage', 'price', 'created']
    default_values = {'created':datetime.datetime.now()}

