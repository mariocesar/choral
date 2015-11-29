import os
from gi.repository import Gio, WebKit2


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class WebView(WebKit2.WebView):
    def __init__(self, app):
        self.app = app
        WebKit2.WebView.__init__(self)

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
        path = os.path.join(ROOT_DIR, 'assets/', request.get_path().lstrip('/'))

        if os.path.exists(path):
            mimetype = self.app.get_mimetype(path)
            request.finish(Gio.File.new_for_path(path).read(None), -1, mimetype)
        else:
            raise Exception('App resource path not found: {0}'.format(path))
