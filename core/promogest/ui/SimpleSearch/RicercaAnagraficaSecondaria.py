# -*- coding: utf-8 -*-

#    Copyright (C) 2005-2012 by Promotux
#                        di Francesco Meloni snc - http://www.promotux.it/

#    Author: Francesco Meloni  <francesco@promotux.it>
#    Author:  Andrea Argiolas   <andrea@promotux.it>
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

from promogest.ui.Ricerca import Ricerca, RicercaFilter
from promogest.dao.AnagraficaSecondaria import AnagraficaSecondaria_
from promogest.lib.utils import showAnagraficaRichiamata, prepareFilterString, findIdFromCombobox
from promogest.ui.gtk_compat import *
from promogest.modules.RuoliAzioni.dao.Role import Role

class RicercaAnagraficaSecondaria(Ricerca):
    """ Ricerca anagrafica secondaria """
    def __init__(self, tipo_dao=None):
        Ricerca.__init__(self, 'Promogest - Ricerca Anagrafica Secondaria',
                        RicercaAnagraficaSecondariaFilter(self, tipo_dao=tipo_dao))
        #self.ricerca_html.destroy()
        self.tipo_dao = tipo_dao


    def insert(self, toggleButton, returnWindow):
        # Richiamo anagrafica di competenza

        def refresh():
            self.filter.refresh()
            self.filter.ragione_sociale_filter_entry.grab_focus()

        from promogest.ui.AnagraficaSecondaria import AnagraficaSecondarie
        role = Role().select(name=self.tipo_dao)
        if role:
            daoRole=role[0]
        anag = AnagraficaSecondarie(daoRole=daoRole)
        anagWindow = anag.getTopLevel()

        showAnagraficaRichiamata(returnWindow, anagWindow, toggleButton, refresh)

        anag.on_record_new_activate(anag.record_new_button)


class RicercaAnagraficaSecondariaFilter(RicercaFilter):
    """ Filtro per la ricerca dei anagrafica secondaria """
    def __init__(self, ricerca, tipo_dao):
        RicercaFilter.__init__(self, ricerca,
                             root="anagrafica_secondaria_filter_vbox",
                               path='_ricerca_secondaria.glade')
        self.ricerca_avanzata_secondaria_filter_vbox.destroy()
        self.ricerca_alignment.destroy()
        self.ricerca = ricerca
        self.tipo_dao = tipo_dao


    def on_filter_treeview_selection_changed(self, treeview):
        pass

    def draw(self):
        # Colonne della Treeview per il filtro
        treeview = self._ricerca.ricerca_filter_treeview
        renderer = gtk.CellRendererText()

        column = gtk.TreeViewColumn('Codice', renderer,text=1)
        column.set_sizing(GTK_COLUMN_GROWN_ONLY)
        column.set_clickable(True)
        column.connect("clicked", self._changeOrderBy, 'codice')
        column.set_resizable(True)
        column.set_expand(False)
        treeview.append_column(column)

        column = gtk.TreeViewColumn('Ragione Sociale', renderer, text=2)
        column.set_sizing(GTK_COLUMN_GROWN_ONLY)
        column.set_clickable(True)
        column.connect("clicked", self._changeOrderBy, 'ragione_sociale')
        column.set_resizable(True)
        column.set_expand(False)
        treeview.append_column(column)

        column = gtk.TreeViewColumn('Cognome - Nome', renderer,text=3)
        column.set_sizing(GTK_COLUMN_GROWN_ONLY)
        column.set_clickable(True)
        column.connect("clicked", self._changeOrderBy, 'cognome, nome')
        column.set_resizable(True)
        column.set_expand(False)
        treeview.append_column(column)

        column = gtk.TreeViewColumn('Localita', renderer,text=4)
        column.set_sizing(GTK_COLUMN_GROWN_ONLY)
        column.set_clickable(True)
        column.connect("clicked", self._changeOrderBy, 'localita')
        column.set_resizable(True)
        column.set_expand(False)
        treeview.append_column(column)

        treeview.set_search_column(1)


        self.clear()

    def clear(self):
        # Annullamento filtro
        self.codice_filter_entry.set_text('')
        self.ragione_sociale_filter_entry.set_text('')
        self.cognome_nome_filter_entry.set_text('')
        self.localita_filter_entry.set_text('')
        self.codice_fiscale_filter_entry.set_text('')
        self.partita_iva_filter_entry.set_text('')
        self.ragione_sociale_filter_entry.grab_focus()
        self.refresh()

    def on_filter_entry_changed(self, text):
        stringa = text.get_text()
        def bobo():
            self.refresh()
        gobject.idle_add(bobo)

    def refresh(self):
        # Aggiornamento TreeView
        codice = prepareFilterString(self.codice_filter_entry.get_text())
        ragioneSociale = prepareFilterString(self.ragione_sociale_filter_entry.get_text())
        #insegna = prepareFilterString(self.insegna_filter_entry.get_text())
        cognomeNome = prepareFilterString(self.cognome_nome_filter_entry.get_text())
        localita = prepareFilterString(self.localita_filter_entry.get_text())
        partitaIva = prepareFilterString(self.partita_iva_filter_entry.get_text())
        codiceFiscale = prepareFilterString(self.codice_fiscale_filter_entry.get_text())
        #idCategoria = findIdFromCombobox(self.id_categoria_cliente_filter_combobox)
        role = Role().select(name=self.tipo_dao)
        if role:
            idRole= role[0].id
        self.numRecords = AnagraficaSecondaria_().count(codice=codice,
                                                    ragioneSociale=ragioneSociale,
                                                    cognomeNome=cognomeNome,
                                                    idRole=idRole,
                                                    localita=localita,
                                                    partitaIva=partitaIva,
                                                    codiceFiscale=codiceFiscale,
                                                    )

        self._refreshPageCount()

        clis = AnagraficaSecondaria_().select(orderBy=self.orderBy,
                                            codice=codice,
                                            ragioneSociale=ragioneSociale,
                                            cognomeNome=cognomeNome,
                                            localita=localita,
                                            idRole=idRole,
                                            partitaIva=partitaIva,
                                            codiceFiscale=codiceFiscale,
                                            offset=self.offset,
                                            batchSize=self.batchSize)

        model = gtk.ListStore(object, str, str, str, str)

        for c in clis:
            model.append((c,
                          (c.codice or ''),
                          (c.ragione_sociale or ''),
                          (c.cognome or '') + ' ' + (c.nome or ''),
                          (c.sede_operativa_localita or '')))

        self._ricerca.ricerca_filter_treeview.set_model(model)
