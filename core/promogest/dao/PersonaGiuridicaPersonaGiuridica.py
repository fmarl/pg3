# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2013 by Promotux
#                       di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni  <francesco@promotux.it>
#    This file is part of Promogest. http://www.promogest.me

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
from promogest.dao.Dao import Dao

try:
    t_personagiuridica_personagiuridica=Table('personagiuridica_personagiuridica',
        params['metadata'],
        schema = params['schema'],
        autoload=True)
except:
    from data.personaGiuridicaPersonaGiuridica import t_personagiuridica_personagiuridica



class PersonaGiuridicaPersonaGiuridica(Dao):
    """  """
    def __init__(self, req=None):
        Dao.__init__(self, entity=self)

    def filter_values(self,k,v):
        if k == 'idPersonaGiuridica':
            dic= {k : t_personagiuridica_personagiuridica.c.id_persona_giuridica == v}
        elif k == 'idPersonaGiuridicaAbbinata':
            dic = {k:t_personagiuridica_personagiuridica.c.id_persona_giuridica_abbinata == v}
        return  dic[k]


std_mapper = mapper(PersonaGiuridicaPersonaGiuridica,
    t_personagiuridica_personagiuridica, properties={},
    order_by=t_personagiuridica_personagiuridica.c.id_persona_giuridica_abbinata)
