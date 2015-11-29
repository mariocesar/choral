from gi.repository import Gtk
from choral.utils import gtk_image_from_icon_name
from .dialogs import SettingsDialog


class Toolbar(Gtk.HeaderBar):
    def __init__(self, window, app):
        super().__init__()
        self.app = app
        self.set_show_close_button(True)
        self.parent = window
        self.props.title = window._title

        headerbar_box = Gtk.Box(Gtk.Orientation.HORIZONTAL, 10)

        self.set_custom_title(headerbar_box)

        menu = Gtk.Menu()

        add_feed_item = Gtk.MenuItem(label="Add Podcast Feed")
        add_feed_item.connect("activate", self.add_feed_selected)
        menu.add(add_feed_item)

        import_item = Gtk.MenuItem(label="Import Subcriptions...")
        import_item.connect("activate", self.import_selected)
        menu.add(import_item)

        export_item = Gtk.MenuItem(label="Export Subscriptions...")
        export_item.connect("activate", self.export_selected)
        menu.add(export_item)

        menu.add(Gtk.SeparatorMenuItem())

        preferences_item = Gtk.MenuItem(label="Preferences")
        preferences_item.connect("activate", self.preferences_selected)
        menu.add(preferences_item)

        menu.show_all()

        app_menu = Gtk.MenuButton(image=gtk_image_from_icon_name('open-menu'))
        app_menu.set_popup(menu)
        app_menu.show_all()

        self.pack_end(app_menu)
        self.set_custom_title(headerbar_box)

    def add_feed_selected(self):
        pass

    def import_selected(self):
        pass

    def export_selected(self):
        pass

    def preferences_selected(self, widget):
        settings_dialog = SettingsDialog(self.parent)
        settings_dialog.show_all()
