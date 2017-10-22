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
import pprint

class Config(object):
    def __init__(self):
        self._username = "USERNAME"
        self._password = "PASSWORD"
        self._host = "MONGO HOST"

    def host(self):
        return  "mongodb://%s:%s@%s" % (self._username,
                                        self._password,
                                        self._host)
