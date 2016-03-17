#!/usr/bin/env python
# -*- coding: utf-8 -*-

import npyscreen
import constants


class Config:

    options = None

    def __init__(self):
        self.options = self.create_config()

    def write_config(self):
        with open(constants.Paths.CONFIG_FILE, 'w') as f:
            for opt in self.options.options:
                    f.write('%s=%s\n' % (opt.get_real_name(), opt.get()))

    def create_config(self):
        opt = npyscreen.OptionList()
        opt.options.append(npyscreen.OptionFreeText(
                       constants.Options.MONGODB_URI,
                       value='localhost'))
        return opt

    def read_config(self):
        try:
            with open(constants.Paths.CONFIG_FILE, 'r') as f:
                for line in f.readlines():
                     line = line.strip()
                     name, value = line.split("=")
                     for option in self.options.options:
                         if option.get_real_name() == name:
                             option.set(value)
            return True
        except:
            return False

