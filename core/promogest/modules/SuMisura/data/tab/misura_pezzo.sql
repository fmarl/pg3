--
-- Copyright (C) 2005 by Promotux Informatica - http://www.promotux.it/
-- Author: JJDaNiMoTh <jjdanimoth@gmail.com>
--
-- This program is free software; you can redistribute it and/or
-- modify it under the terms of the GNU General Public License
-- as published by the Free Software Foundation; either version 2
-- of the License, or (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program; if not, write to the Free Software
-- Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

/*

misura_pezzo - Tabella delle misure dei pezzi

*/

DROP TABLE misura_pezzo CASCADE;

DROP SEQUENCE misura_pezzo_id_seq;
CREATE SEQUENCE misura_pezzo_id_seq;

CREATE TABLE misura_pezzo (
      id                        bigint          
    DEFAULT NEXTVAL('misura_pezzo_id_seq') PRIMARY KEY NOT NULL
        ,altezza     decimal(16,4)   NOT NULL
        ,larghezza   decimal(16,4)   NOT NULL
        ,moltiplicatore decimal(16,4) NULL
        -- Chiavi esterne
        ,id_riga                bigint         
    NOT NULL REFERENCES riga ( id ) 
    ON UPDATE CASCADE ON DELETE RESTRICT

    ,UNIQUE(id_riga)

    );
