import logging
import time
from itertools import chain

logger = logging.getLogger('choral')

tabbing = 0


def log(fn):
    # from gnome-music
    if logger.getEffectiveLevel() != logging.DEBUG:
        return fn

    def wrapped(*v, **k):
        global tabbing
        name = fn.__qualname__
        filename = fn.__code__.co_filename.split('/')[-1]
        lineno = fn.__code__.co_firstlineno

        params = ", ".join(map(repr, chain(v, k.values())))

        if 'rateLimitedFunction' not in name:
            logger.debug("%s%s(%s)[%s:%s]",
                         '|' * tabbing, name, params, filename, lineno, )
        tabbing += 1
        start = time.time()
        retval = fn(*v, **k)
        elapsed = time.time() - start
        tabbing -= 1
        elapsed_time = ''
        if elapsed > 0.1:
            elapsed_time = ', took %02f' % elapsed
        if elapsed_time or retval is not None:
            if 'rateLimitedFunction' not in name:
                logger.debug("%s  returned %s%s", '|' * tabbing, repr(retval), elapsed_time)

        return retval

    return wrapped
