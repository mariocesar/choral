from gi.repository import Gtk


def build_css_provider(path):
    provider = Gtk.CssProvider()

    with open(path, 'r') as f:
        provider.load_from_data(f.read().encode('UTF-8'))

    return provider


def gtk_image_from_theme(theme, icon_name, size=Gtk.IconSize.LARGE_TOOLBAR):
    pix = theme.load_icon(icon_name, size, 0)
    img = Gtk.Image()
    img.set_from_pixbuf(pix)
    return img


def gtk_image_from_icon_name(icon_name, size=Gtk.IconSize.LARGE_TOOLBAR):
    img = Gtk.Image()
    img.set_from_icon_name(icon_name, size)
    return img
