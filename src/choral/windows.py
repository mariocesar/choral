from .base import BaseWindow
from .widgets.toolbar import Toolbar


class MainWindow(BaseWindow):
    _title = 'Choral'
    _name = 'choral'
    _stylesheet = 'assets/styles.css'

    def __init__(self, app, screen):
        super().__init__(app, screen)

        self.set_size_request(
            width=self.app.settings.window_width,
            height=self.app.settings.window_height)

        self.toolbar = Toolbar(self, app)
        self.toolbar.get_style_context().add_class(".headerbar")
        self.set_titlebar(self.toolbar)
