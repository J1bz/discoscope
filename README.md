discoscope
==========

Discoscope is a discord bot allowing users ask the bot `whois <whatever>`. The
bot will then reply if it knows what the user asked for.

The response is based on a key/value system.

This bot has been designed to display pictures (since discord supports many
thumbnails, including images), hence `scope` in the name.

Installation
------------

    sudo aptitude install python-virtualenv git

    virtualenv -p python3 venv_discoscope
    source venv_discoscope/bin/activate

    git clone https://github.com/b1naryth1ef/disco/
    cd disco
    python setup.py install  # may take some time to compile gevent
    cd ..

    git clone https://github.com/J1bz/discoscope
    cd discoscope
    cp config.json_DIST config.json
    cp whois.json_DIST whois.json

Update `config.json` with your own bot token, then :

    python -m disco.cli

Features
--------

If you edit `whois.json`, the plugin will know it and reload its cache,
allowing you to make live modifications with no downtime. Pretty cool !
