# xymon-monitors
Scripts for monitoring services

# Requriements
* Python 3

# Installaton
Use `-e` on pip to get an editable copy of the source in `./src`.
## Virtualenv
```bash
$ mkdir xymon-monitors && cd $_
$ virtualenv -p $(which python3) venv
$ source venv/bin/activate
$ pip install "git+https://github.com/UniversityRadioYork/xymon-monitors.git#egg=xymon-monitors"
```
## Global
```bash
$ sudo pip install "git+https://github.com/UniversityRadioYork/xymon-monitors.git#egg=xymon-monitors"
```
## Local (without virtualenv, into ~/.local or something):
```bash
$ pip install --user "git+https://github.com/UniversityRadioYork/xymon-monitors.git#egg=xymon-monitors"
```

# Development
```bash
$ python setup.py clean
$ python setup.py build
$ python setup.py install
```

# Use
## Running
The scripts will be installed by setuptools. See `console-scripts` in `setup.py`.
For example, ```$ icecast_json```.
## Crontab
The scripts are intended to be run by something like ```cron```.
```bash
$ sudo EDITOR=myeditor crontab -u xymon -e
```
```bash
PATH=/usr/local/bin
*/5 * * * * icecast_json
```
## Output
Log files will be stored in one of these directories on the machine which runs them (descending preference): `/var/log/xymon/`, `/var/log/hobbit/`, or `~`.

# Xymon
## Server
Xymon must be configured to trigger a status on  `SUCCESS` or `ERROR` in the logs.

This will affect the `msgs` service on the host where the script runs.
* `analysis.cfg`:
```bash
HOST=myhost
LOG /var/log/hobbit/icecast_json.log SUCCESS COLOR=green
LOG /var/log/hobbit/icecast_json.log ERROR
```
* `client-local.cfg`:
```bash
[host=myhost]
log:/var/log/hobbit/icecast_json.log:10240
```
A reload or restart of Xymon is required.

# Bugs
Xymon is supposed to read new log lines each time there's a client update, but I couldn't get it to work quite right. To overcome this, the scripts overwrite their logs.
