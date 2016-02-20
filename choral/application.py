import os
import logging
import magic

from gi.repository import Gtk, Gdk, GLib, Gio

from choral.window import MainWindow
from choral.conf import settings

logger = logging.getLogger('choral')


class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id=settings.namespace)

        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = MainWindow(self)
            self.window.show_all()

            logger.debug('do_activate: Make window application')
        else:
            logger.debug('do_activate: Make window present')
            self.window.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        Gdk.set_program_class('choral')
        GLib.set_prgname('choral')

        with open(os.path.join(settings.BASE_DIR, 'assets/css/gtk-ui.css'), 'r') as f:
            stylesheet = f.read().encode('UTF-8')
            self.set_theming(stylesheet, 'choral')

        self.mime = magic.Magic(mime=True)
        self.theme = Gtk.IconTheme.get_default()

        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', self.about_callback)
        self.add_action(about_action)

        help_action = Gio.SimpleAction.new("help", None)
        help_action.connect("activate", self.help_callback)
        self.add_action(help_action)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_callback)
        self.add_action(quit_action)

    def about_callback(self, *args):
        logger.debug('About dialog')

        builder = Gtk.Builder()
        builder.add_from_file(os.path.join(settings.BASE_DIR, 'ui/aboutdialog.ui'))

        about = builder.get_object('aboutdialog')
        about.set_transient_for(self.window)
        about.connect("response", lambda dialog, response: dialog.destroy())
        about.show()

    def help_callback(self):
        logger.warning('Help not implemented yet')

    def quit_callback(self):
        self.quit()

    def set_theming(self, stylesheet: bytes, class_name: str = None):
        logger.debug('Setting theming with %s' % stylesheet)

        screen = Gdk.Screen.get_default()
        context = Gtk.StyleContext()

        if class_name:
            context.add_class(class_name)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(stylesheet)

        context.add_provider_for_screen(
            screen, css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
