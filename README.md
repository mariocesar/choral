# Choral

A fork/rewrite of Nathan Dyer's vocal app made in Python/Gtk3

Using Python 3.4.3

# Running in develop

    git clone git@github.com:mariocesar/choral-app.git
    cd choral-app/
    virtualenv --python=/usr/bin/python3.4 env
    source env/bin/activate
    (venv) pip install -e .
    (venv) python -m choral

# Current status:

![Screnshot](https://raw.githubusercontent.com/mariocesar/choral-app/master/screenshot.png)

- [ ] New branding?
- [ ] Download and Update manager in a second process (As a service)

# Common issues

## Development Requiments in Ubuntu/Debian

You may need:

    sudo apt-get install python3-gi gir1.2-gtk-3.0 gir1.2-webkit2-3.0

## Missing accessibility bus:

If you see this warning:

    ** (__main__.py:5684): WARNING **: Couldn't connect to accessibility bus: Failed to connect to socket /tmp/dbus-bIKmAltvbA: Connection refused

You could either dismiss it, or run the app with the command bellow,
to hide that warning.

    NO_AT_BRIDGE=1 python -m choral
