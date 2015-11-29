import magic
from gi.repository import Gtk, Gio

from .windows import MainWindow
from .settings import ChoralSetttings

mime = magic.open(magic.MAGIC_MIME)
mime.load()


class Application(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(
            self,
            application_id='net.launchpad.choral',
            flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        Gtk.Application.do_activate(self)

        self.settings = ChoralSetttings()
        self.theme = Gtk.IconTheme.get_default()

        self.window = MainWindow(self)
        self.window.show_all()
        self.add_window(self.window)

    def get_mimetype(self, path):
        return mime.file(path)
