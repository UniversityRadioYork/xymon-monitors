#!/usr/bin/env python3


def main():
        import urllib.request
        import json
        import xymon_monitors.logging
        import logging

        xymon_monitors.logging.configure('icecast_json')
        l = logging.getLogger()

        error = False
        try:
                r = urllib.request.urlopen("https://ury.org.uk/audio/json2.xsl").read()
        except:
                l.exception('Icecast JSON unavailable')
                error = True

        try:
                json.loads(str(r, 'utf-8').replace('\\n', '\n'))
        except NameError:  # Skip
                pass
        except:
                l.exception('Could not parse Icecast JSON')
                error = True

        if not error:
                l.info('SUCCESS:Icecast JSON working')

if __name__ == '__main__':
        main()
