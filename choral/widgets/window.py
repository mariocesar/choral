from gi.repository import Gtk, Gdk


class Window(Gtk.ApplicationWindow):
    _title = None
    _name = None
    _resizable = True
    _keep_above = False
    _position = Gtk.WindowPosition.CENTER
    _gravity = Gdk.Gravity.SOUTH_EAST
    _type_hint = Gdk.WindowTypeHint.NORMAL

    def __init__(self, app):
        super().__init__(application=app, title=self._title)

        self.set_name(self.name)
        self.set_title(self.title)
        self.set_resizable(self._resizable)
        self.set_keep_above(self._keep_above)
        self.set_gravity(self._gravity)
        self.set_position(self._position)
        self.set_type_hint(self._type_hint)

    @property
    def title(self):
        return 'Window title' if not self._title else self._title

    @property
    def name(self):
        return 'window' if not self._name else self._name
