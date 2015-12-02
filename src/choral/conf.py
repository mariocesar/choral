import os


class BaseSettings:
    namespace = None


class ChoralSetttings(BaseSettings):
    namespace = "net.launchpad.choral"

    WINDOW_WIDTH = 990
    WINDOW_HEIGHT = 525
    LIBRARY_LOCATION = None
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


settings = ChoralSetttings()
