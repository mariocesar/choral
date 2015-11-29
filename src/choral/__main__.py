from .application import Application


if __name__ == "__main__":
    from gi.repository import Gdk, GLib
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    Gdk.set_program_class('choral')
    GLib.set_prgname('choral')

    application = Application()
    application.run(None)
