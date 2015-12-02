from choral.conf import settings
from choral.widgets.toolbar import Toolbar
from choral.widgets.webview import WebView
from choral.widgets.window import Window


class MainWindow(Window):
    _title = 'Choral'
    _name = 'main-window'

    def __init__(self, app):
        super().__init__(app)

        self.set_size_request(
            width=settings.WINDOW_WIDTH,
            height=settings.WINDOW_HEIGHT)

        self.toolbar = Toolbar(self, app)
        self.toolbar.set_show_close_button(True)
        self.toolbar.get_style_context().add_class(".headerbar")
        self.toolbar.show()
        self.set_titlebar(self.toolbar)

        self.webview = WebView(app)
        self.webview.load_uri('choral:///app.html')
        self.webview.show()

        self.add(self.webview)
