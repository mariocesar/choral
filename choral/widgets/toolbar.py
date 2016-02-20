import logging

from gi.repository import Gtk
from choral.utils import gtk_image_from_icon_name
from choral.widgets.dialogs import SettingsDialog

logger = logging.getLogger('choral')


class Toolbar(Gtk.HeaderBar):
    def __init__(self, window, app: Gtk.Application):
        super().__init__()
        self.app = app
        self.set_show_close_button(True)
        self.parent = window
        self.props.title = window._title

        headerbar_box = Gtk.Box(Gtk.Orientation.HORIZONTAL, 10)

        self.set_custom_title(headerbar_box)

        add_feed_item = Gtk.MenuItem(label="Add Podcast Feed")
        add_feed_item.connect("activate", self.add_feed_selected)

        import_item = Gtk.MenuItem(label="Import Subcriptions...")
        import_item.connect("activate", self.import_selected)

        export_item = Gtk.MenuItem(label="Export Subscriptions...")
        export_item.connect("activate", self.export_selected)

        preferences_item = Gtk.MenuItem(label="Preferences")
        preferences_item.connect("activate", self.preferences_selected)

        about_item = Gtk.MenuItem(label="About")
        about_item.connect("activate", self.app.about_callback)

        menu = Gtk.Menu()
        menu.add(add_feed_item)
        menu.add(import_item)
        menu.add(export_item)
        menu.add(Gtk.SeparatorMenuItem())
        menu.add(preferences_item)
        menu.add(about_item)

        menu.show_all()

        app_menu = Gtk.MenuButton(image=gtk_image_from_icon_name('open-menu'))
        app_menu.set_popup(menu)
        app_menu.show_all()

        self.pack_end(app_menu)
        self.set_custom_title(headerbar_box)

    def add_feed_selected(self, widget):
        logger.info('Add feed dialog')

    def import_selected(self, widget):
        logger.info('Import feed dialog')

    def export_selected(self, widget):
        logger.info('Export feed dialog')

    def preferences_selected(self, widget):
        logger.info('Preferences dialog')
        settings_dialog = SettingsDialog(self.parent)
        settings_dialog.show_all()
