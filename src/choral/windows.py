from .base import BaseWindow
from .widgets.toolbar import Toolbar
from .widgets.webview import WebView


class MainWindow(BaseWindow):
    _title = 'Choral'
    _name = 'main-window'
    _stylesheet = 'assets/css/gtk-ui.css'

    def __init__(self, app):
        super().__init__(app)

        self.set_size_request(
            width=self.app.settings.window_width,
            height=self.app.settings.window_height)

        self.toolbar = Toolbar(self, app)
        self.toolbar.set_show_close_button(True)
        self.toolbar.get_style_context().add_class(".headerbar")
        self.set_titlebar(self.toolbar)

        webview = WebView(app)
        webview.load_uri('choral:///app.html')
        webview.show()

        self.add(webview)
