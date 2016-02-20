from gi.repository import Gtk


class SettingsDialog(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__()
        headerbar = Gtk.HeaderBar(title='Preferences')
        headerbar.set_has_subtitle(False)
        headerbar.set_show_close_button(False)
        headerbar.get_style_context().remove_class("header-bar")

        self.set_titlebar(headerbar)
        self.set_title('Preferences')
        self.set_modal(True)
        self.set_transient_for(parent)

        content = self.get_content_area()
        content.homogeneous = False
        content.margin_left = 12
        content.margin_right = 12

        close_button = Gtk.Button(label="Close")
        close_button.connect("clicked", self.close_dialog)
        close_button.margin_bottom = 12
        close_button.margin_right = 5

        button_box = Gtk.ButtonBox()
        button_box.set_layout(Gtk.ButtonBoxStyle.END)
        button_box.pack_end(close_button, False, False, 12)

        content.add(button_box)

    def close_dialog(self, widget):
        self.destroy()
