import magic
from gi.repository import Gtk

from .windows import MainWindow
from .settings import ChoralSetttings

mime = magic.open(magic.MAGIC_MIME)
mime.load()


class Application(Gtk.Application):
    def do_activate(self):
        self.settings = ChoralSetttings()
        self.theme = Gtk.IconTheme.get_default()

        self.window = MainWindow(self)
        self.window.connect('destroy', Gtk.main_quit)
        self.window.show_all()

        self.add_window(self.window)

    def get_mimetype(self, path):
        return mime.file(path)
