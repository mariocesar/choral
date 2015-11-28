from gi.repository import Gtk


def build_css_provider(path):
    provider = Gtk.CssProvider()

    with open(path, 'r') as f:
        provider.load_from_data(f.read().encode('UTF-8'))

    return provider
