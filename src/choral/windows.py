import os
from gi.repository import Gtk, Gdk

from .utils import build_css_provider
from .widgets.toolbar import Toolbar


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

    def __init__(self, app, screen):
        super().__init__()
        self.app = app
        self.set_css_style(screen)
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

    @property
    def stylesheet(self):
        if self._stylesheet:
            return os.path.join(ROOT_PATH, self._stylesheet)
        return None

    def set_css_style(self, screen):
        css_provider = build_css_provider(self.stylesheet)
        context = self.get_style_context()
        context.add_provider_for_screen(
            screen, css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


class MainWindow(BaseWindow):
    _title = "Choral"
    _name = "choral"
    _stylesheet = 'assets/styles.css'

    def __init__(self, app, screen):
        super().__init__(app, screen)

        self.set_size_request(
            width=self.app.settings.window_width,
            height=self.app.settings.window_height)

        self.toolbar = Toolbar(self, app)
        self.toolbar.get_style_context().add_class(".headerbar")
        self.set_titlebar(self.toolbar)
