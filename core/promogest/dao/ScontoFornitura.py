# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2012 by Promotux
#                       di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni  <francesco@promotux.it>
#    Author: Francesco Marella <francesco.marella@anche.no>

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
from sqlalchemy.orm import *
from promogest.Environment import *

try:
    t_sconto_fornitura = Table('sconto_fornitura',
                           params['metadata'],
                           schema=params['schema'],
                           autoload=True)
except:
    from data.sconto import t_sconto
    from data.scontoFornitura import t_sconto_fornitura


from promogest.dao.Dao import Dao
from promogest.dao.Sconto import t_sconto


class ScontoFornitura(Dao):
    """  """
    def __init__(self, req=None):
        Dao.__init__(self, entity=self)

    def filter_values(self, k, v):
        dic = {'idFornitura': t_sconto_fornitura.c.id_fornitura==v}
        return dic[k]



std_mapper = mapper(ScontoFornitura,
    join(t_sconto, t_sconto_fornitura),
    properties={
        'id': [t_sconto.c.id, t_sconto_fornitura.c.id]
    },
    order_by=t_sconto_fornitura.c.id)
