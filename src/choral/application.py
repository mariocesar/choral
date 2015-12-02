import os
import magic
from gi.repository import Gtk, Gdk, GLib, Gio

from choral import log
from choral.window import MainWindow
from choral.conf import settings
import logging

logger = logging.getLogger(__name__)


class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(
            self,
            application_id='net.launchpad.choral',
            flags=Gio.ApplicationFlags.FLAGS_NONE)

        Gdk.set_program_class('choral')
        GLib.set_prgname('choral')

        with open(os.path.join(settings.BASE_DIR, 'assets/css/gtk-ui.css'), 'r') as f:
            stylesheet = f.read().encode('UTF-8')
            self.set_theming(stylesheet, 'choral')

        self._mime = magic.open(magic.MAGIC_MIME)
        self._mime.load()

    @log
    def do_activate(self):
        Gtk.Application.do_activate(self)
        self.theme = Gtk.IconTheme.get_default()
        self.window = MainWindow(self)
        self.window.show_all()
        self.add_window(self.window)

        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', self.about_dialog)
        self.add_action(about_action)

    @log
    def about_dialog(self, *args):
        builder = Gtk.Builder()
        builder.add_from_file(os.path.join(settings.BASE_DIR, 'ui/aboutdialog.ui'))
        about = builder.get_object('aboutdialog')
        about.set_transient_for(self.window)
        about.connect("response", lambda dialog, response: dialog.destroy())
        about.show()

    @log
    def quit(self, action=None, param=None):
        self.window.destroy()

    @log
    def get_mimetype(self, path):
        return self._mime.file(path)

    @log
    def set_theming(self, stylesheet: bytes, class_name: str = None):
        screen = Gdk.Screen.get_default()
        context = Gtk.StyleContext()

        if class_name:
            context.add_class(class_name)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(stylesheet)

        context.add_provider_for_screen(
            screen, css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
