import os
import choral


class BaseSettings:
    @property
    def author(self):
        return '%s <%s>' % (choral.__author, choral.__author_email__)

    @property
    def version(self):
        return choral.__version__

    @property
    def data_dir(self):
        return choral.__data_dir__

    @property
    def namespace(self):
        return choral.__application_id__

    @property
    def main_url(self):
        return choral.__main_url__

    @property
    def bug_url(self):
        return choral.__bug_url__


class ChoralSetttings(BaseSettings):
    WINDOW_WIDTH = 990
    WINDOW_HEIGHT = 525
    LIBRARY_LOCATION = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


settings = ChoralSetttings()
