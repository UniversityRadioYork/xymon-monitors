from os import path
import logging


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
