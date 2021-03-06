# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2013 by Promotux
#                        di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni  <francesco@promotux.it>

#    This file is part of Promogest.

#    Promogest is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.

#    Promogest is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Promogest.  If not, see <http://www.gnu.org/licenses/>.


from sqlalchemy import *

class AppLogDb(object):

    def __init__(self, schema = None,mainSchema=None, metadata=None, session=None,debug=False):
        self.metadata = metadata
        self.schema = schema
        self.mainSchema = mainSchema
        self.debug = debug

    def create(self):
        app_table = Table('app_log', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('id_utente', Integer),
            Column('utentedb', String(100), nullable=False),
            Column('schema_azienda', String(100), nullable=False),
            Column('level', String(1)),
            Column('object', PickleType, nullable=True),
            Column('message', String(1000), nullable=True),
            Column('value', Integer, nullable=True),
            Column('registration_date', DateTime),
            schema=self.mainSchema)

        app_table.create(checkfirst=True)


    def alter(self, req=None, arg=None):
        pass
