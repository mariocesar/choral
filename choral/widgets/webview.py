import os
import logging

from gi.repository import Gtk, Gio, WebKit2
from choral.conf import settings

logger = logging.getLogger('choral.webview')


class WebView(WebKit2.WebView):
    def __init__(self, app: Gtk.Application):
        WebKit2.WebView.__init__(self)
        self.app = app

        context = WebKit2.WebContext.get_default()
        context.register_uri_scheme('choral', self.request_callback)

        manager = context.get_security_manager()
        manager.register_uri_scheme_as_cors_enabled('choral')

        settings = self.get_settings()
        settings.set_property("enable-developer-extras", True)
        settings.set_property("enable-accelerated-2d-canvas", True)
        settings.set_property("enable-smooth-scrolling", True)
        settings.set_property("javascript-can-access-clipboard", True)

        settings.set_enable_fullscreen(False)
        settings.set_enable_plugins(False),
        settings.set_enable_page_cache(False)
        settings.set_enable_dns_prefetching(True)

    def request_callback(self, request):
        logger.info('webview: GET %s', request.get_path())
        path = os.path.join(settings.BASE_DIR, 'assets/', request.get_path().lstrip('/'))

        if os.path.exists(path):
            mimetype = self.app.mime.from_file(path).decode()
            request.finish(Gio.File.new_for_path(path).read(None), -1, mimetype)
        else:
            logger.exception('App resource path not found: {0}'.format(path))
