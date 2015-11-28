from gi.repository import Gtk, Gdk

from .windows import MainWindow


class Application(Gtk.Application):
    def do_activate(self):
        screen = Gdk.Screen.get_default()

        self.window = MainWindow(self, screen)

        self.add_window(self.window)
        self.window.show_all()
