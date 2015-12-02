import logging
from gi.repository import Gtk

logger = logging.getLogger(__name__)


def gtk_image_from_theme(theme, icon_name, size=Gtk.IconSize.LARGE_TOOLBAR):
    pix = theme.load_icon(icon_name, size, 0)
    img = Gtk.Image()
    img.set_from_pixbuf(pix)
    return img


def gtk_image_from_icon_name(icon_name, size=Gtk.IconSize.LARGE_TOOLBAR):
    img = Gtk.Image()
    img.set_from_icon_name(icon_name, size)
    return img
