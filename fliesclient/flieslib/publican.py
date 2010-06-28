# vim:set et sts=4 sw=4: 
# 
# Flies Python Client
#
# Copyright (c) 2010 Jian Ni <jni@gmail.com>
# Copyright (c) 2010 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330,
# Boston, MA  02111-1307  USA

__all__ = (
            "Publican",
          )

import polib

class Publican:
    def __init__(self, filepath):
        self.path = filepath
	    
    def read_po(self):
        po = polib.pofile(self.path)
        id = 1
        textflows = []
        for entry in po:
            textflowId = 'tf'+str(id)
            textflow = {
                'id' : textflowId,
                'lang' : 'en',
                'content' : entry.msgid,
                'extensions' : []}
            textflows.append(textflow)
            id = id+1
        return textflows
 
    def load_po(self):
        return polib.pofile(self.path)

    def create(self):
        pass
       