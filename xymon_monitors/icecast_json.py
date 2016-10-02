#!/usr/bin/env python3
import logging
import xymon_monitors.logging as xm_logging
import urllib.request
import json

l = logging.getLogger()
xm_logging.configure('icecast_json')


@xm_logging.exception_quit(l, Exception, 'Icecast JSON unavailable')
def get_HTTP(url):
    return urllib.request.urlopen(url).read()


@xm_logging.exception_quit(l, Exception, 'Could not parse Icecast JSON')
def parse_json(s):
    try:
        json.loads(str(r, 'utf-8').replace('\\n', '\n'))
    except NameError:
        pass  # Skip


@xm_logging.exception_quit(l, Exception, 'Unknown exception thrown')
def main():
    r = get_HTTP('https://ury.org.uk/audio/status-json.xsl')
    parse_json(r)

    l.info('SUCCESS:Icecast JSON working')


if __name__ == '__main__':
    main()
