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

import os
import locale
import gettext

def bindtextdomain(app_name, locale_dir=None):
    """
    Bind the domain represented by app_name to the locale directory locale_dir.
    It has the effect of loading translations, enabling applications for different
    languages.

    app_name:
        a domain to look for translations, tipically the name of an application.

    locale_dir:
        a directory with locales like locale_dir/lang_isocode/LC_MESSAGES/app_name.mo
        If omitted or None, then the current binding for app_name is used.
    """
    # installa _() e ngettext() builtin
    gettext.install(app_name, localedir=locale_dir,
                    names=("ngettext",))
    try:
        locale.bindtextdomain(app_name, locale_dir)
        locale.bind_textdomain_codeset(app_name, "UTF-8")
    except AttributeError:
        pass

    try:
        locale.setlocale(locale.LC_ALL, "")
    except locale.Error as e:
        pass
