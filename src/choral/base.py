import os
from gi.repository import Gtk, Gdk


# TODO: Move to a environnment object
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class BaseWindow(Gtk.Window):
    _title = None
    _name = None
    _stylesheet = None
    _resizable = True
    _keep_above = False
    _position = Gtk.WindowPosition.CENTER
    _gravity = Gdk.Gravity.SOUTH_EAST
    _type_hint = Gdk.WindowTypeHint.NORMAL

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.set_application(app)
        self.set_name(self.name)
        self.set_title(self.title)
        self.set_resizable(self._resizable)
        self.set_keep_above(self._keep_above)
        self.set_gravity(self._gravity)
        self.set_position(self._position)
        self.set_type_hint(self._type_hint)

        if self._stylesheet:
            with open(os.path.join(ROOT_PATH, self._stylesheet), 'r') as f:
                stylesheet = f.read().encode('UTF-8')

            self.set_theming(stylesheet, self._name)

    @property
    def title(self):
        return 'Window title' if not self._title else self._title

    @property
    def name(self):
        return 'window' if not self._name else self._name

    def set_theming(self, stylesheet: str, class_name: str=None):

        screen = Gdk.Screen.get_default()
        context = self.get_style_context()

        if class_name:
            context.add_class(class_name)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(stylesheet)

        context.add_provider_for_screen(
            screen, css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def restore_position(self):
        try:
            x, y = self.app.settings['window-position']
        except ValueError:
            self.set_position(Gtk.WindowPosition.CENTER)
        else:
            self.move(x, y)

    def save_position(self, widget, event):
        self.app.settings['window-position'] = widget.get_position()
