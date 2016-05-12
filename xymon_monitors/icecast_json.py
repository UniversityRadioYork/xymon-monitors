#!/usr/bin/env python3


def main():
        import urllib.request
        import json
        import logging

        logging.basicConfig(level=logging.INFO,
                            filename='/var/log/xymon/icecast_json.log',
                            filemode='w',
                            format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

        error = False
        try:
                r = urllib.request.urlopen("https://ury.org.uk/audio/json2.xsl").read()
        except:
                logging.exception('Icecast JSON unavailable')
                error = True

        try:
                json.loads(str(r, 'utf-8').replace('\\n', '\n'))
        except NameError:  # Skip
                pass
        except:
                logging.exception('Could not parse Icecast JSON')
                error = True

        if not error:
                logging.info('SUCCESS:Icecast JSON working')

if __name__ == '__main__':
        main()
