from os import path
import logging
import sys


def configure(logname,
              level=logging.INFO,
              filemode='w',
              format='%(asctime)s:%(name)s:%(levelname)s:%(message)s'):
    logging.basicConfig(level=logging.INFO,
                        filename=getLogPath(logname),
                        filemode=filemode,
                        format=format)


def getLogPath(logname):
    logdir = ''
    for p in ['/var/log/xymon', '/var/log/hobbit', path.expanduser("~")]:
        if path.exists(p):
            logdir = p
            break
    return path.join(logdir, '{0}.log'.format(logname))


def exception_quit(logger, ex, error_string):
    def pawrappa(func):
        def wrapper(*args, **kw):
            error = False
            try:
                r = func(*args, **kw)
            except ex:
                error = True
                # Print exception before our own line (for Xymon to read)
                logger.exception('Known exception thrown')

            if error:
                logger.error(error_string)
                sys.exit(1)
            else:
                return r
        return wrapper
    return pawrappa
