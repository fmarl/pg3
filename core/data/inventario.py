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

class InventarioDb(object):

    def __init__(self, schema = None,mainSchema=None, metadata=None, session=None,debug=False):
        self.metadata = metadata
        self.schema = schema
        self.debug = debug

    def create(self):
        azTable = Table('magazzino', self.metadata, autoload=True, schema=self.schema)
        bbTable = Table('articolo', self.metadata, autoload=True, schema=self.schema)
        if self.schema:
            magazzinoFK =self.schema+'.magazzino.id'
            articoloFK =self.schema+'.articolo.id'
        else:
            magazzinoFK ='magazzino.id'
            articoloFK = 'articolo.id'


        inventarioTable = Table('inventario', self.metadata,
                Column('id',Integer,primary_key=True),
                Column('anno',Integer,nullable=False),
                Column('id_magazzino',Integer,ForeignKey(magazzinoFK,onupdate="CASCADE",ondelete="CASCADE"),nullable=False),
                Column('id_articolo',Integer,ForeignKey(articoloFK,onupdate="CASCADE",ondelete="CASCADE"),nullable=False),
                Column('quantita',Numeric(16,4),nullable=True),
                Column('valore_unitario',Numeric(16,4),nullable=True),
                Column('data_aggiornamento',DateTime,nullable=True),
                schema=self.schema
                )
        inventarioTable.create(checkfirst=True)

    def update(self, req=None, arg=None):
        pass

    def alter(self, req=None, arg=None):
        pass