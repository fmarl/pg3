# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2013 by Promotux
#                        di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni <francesco@promotux.it>

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

from promogest import Environment
import promogest.ui.Login
from promogest.modules.CSA.ui.AnagraficaServCSA import AnagraficaServCSA

MODULES_NAME = "CSA"
MODULES_FOR_EXPORT = ["CSA"]
GUI_DIR = Environment.cartella_moduli+ '/CSA/gui/'
START_CALL_IS_IN_THREAD = True        # False if you  do NOT want to put execution
START_CALL = None                              # of this call in a separated Thread
TEMPLATES = Environment.cartella_moduli+'/CSA/templates/'

class CSA(object):
    VIEW_TYPE = ('anagrafica', 'CSA', 'taglia48x48.png')
    def getApplication(self):
        anag = AnagraficaServCSA()
        return anag
