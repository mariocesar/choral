import os
from gi.repository import Gtk, Gdk

from .utils import build_css_provider

# TODO: Move to a environnment object
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class MainWindow(Gtk.Window):
    _title = "Choral"
    _name = "choral"
    _stylesheet = os.path.join(ROOT_PATH, 'assets/styles.css')

    def set_css_style(self, screen):
        css_provider = build_css_provider(self._stylesheet)
        context = self.get_style_context()
        context.add_provider_for_screen(
            screen, css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def __init__(self, application, screen):
        super(MainWindow, self).__init__()
        self.application = application
        self.set_css_style(screen)

        self.set_name(self._name)
        self.set_title(self._title)
        self.set_resizable(True)
        self.set_keep_above(True)
        self.set_size_request(460, 500)
        self.set_border_width(10)
        self.set_gravity(Gdk.Gravity.SOUTH_EAST)
        self.set_type_hint(Gdk.WindowTypeHint.NORMAL)
        self.set_position = Gtk.WindowPosition.CENTER

        hb = Gtk.HeaderBar()
        hb.get_style_context().add_class(".headerbar")
        hb.set_show_close_button(True)
        hb.props.title = self._title
        self.set_titlebar(hb)
