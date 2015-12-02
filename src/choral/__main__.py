import logging
import sys
import signal
from colorlog import ColoredFormatter
import gi

formatter = ColoredFormatter(
    "%(log_color)s[%(levelname)s %(asctime)s]%(reset)s %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'purple',
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bg_red',
    }
)
logger = logging.getLogger('choral')

handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def install_excepthook():
    """ Make sure we exit when an unhandled exception occurs. """
    from gi.repository import Gtk
    old_hook = sys.excepthook

    def new_hook(etype, evalue, etb):
        old_hook(etype, evalue, etb)
        while Gtk.main_level():
            Gtk.main_quit()
        sys.exit()

    sys.excepthook = new_hook


if __name__ == "__main__":
    gi.require_version('GIRepository', '2.0')
    gi.require_version('Gtk', '3.0')
    install_excepthook()

    from choral.application import Application

    application = Application()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    status = application.run(sys.argv)
    sys.exit(status)
