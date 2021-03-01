# window.py
#
# Copyright 2021 Giorgio Dramis
#
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

import gi

gi.require_version('Handy', '1')

from gi.repository import Gtk, Handy

@Gtk.Template(resource_path='/org/scroker/HandyTestLayout/window.ui')
class HandyTestLayoutWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'HandyTestLayoutWindow'

    deck = Gtk.Template.Child()
    row = Gtk.Template.Child()
    button_back = Gtk.Template.Child()

    def __init__(self, **kwargs):
        Handy.init()
        super().__init__(**kwargs)
        self.row.connect('key-press-event', self.on_button_click)
        self.button_back.connect('clicked', self.on_button_back_click)

    def on_button_click(self, widget):
        self.deck.set_visible_child_name('hello_word_deck')

    def on_button_back_click(self, widget):
        self.deck.set_visible_child_name('button_deck')
