#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser

def configuration(conf="~/.matomat.conf"):

    config = dict()
    c = ConfigParser.ConfigParser()

    if not c.read(os.path.expanduser(conf)):
        print("Error: your con %s could not be read" % conf)
        exit(1)

    try:
        config["uri"] = c.get("General", "MongoDB")
    except ConfigParser.NoOptionError:
        print("Error: Please set a MongoDB Connection URI in %s" % conf)
        exit(1)

    return config
