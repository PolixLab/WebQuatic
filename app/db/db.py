#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# Copyright 2017 Paul Barajas <paul.barajas@linux.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from pymongo import MongoClient
from config import Config
import pprint

class Singleton(object):
    _instance = None
    def __init__(self, _class):
        self._class =  _class

    def  __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls._class(*args, **kwargs)
            return cls._instance
        return cls._instance

@Singleton
class Connection(Config):

    def __init__(self):
        Config.__init__(self)
        print(self.host())
        self.client = MongoClient(self.host())
        self.db  = self.client.centauro
        self.collection = self.db.clients

    def find_all(self):
        pprint.pprint(self.collection.find_one())
