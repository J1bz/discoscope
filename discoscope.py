import os

from json import loads
from datetime import datetime

from disco.bot.plugin import Plugin
from disco.util.logging import LoggingClass


class Discoscope(Plugin, LoggingClass):
    whois_file = 'whois.json'
    last_whois_update = datetime.now().timestamp()
    _whois_table = None

    @property
    def whois_table(self):
        new_table = self.last_whois_update < os.path.getmtime(self.whois_file)
        if not self._whois_table or new_table:
            with open(self.whois_file, 'r') as fh:
                self._whois_table = loads(fh.read())

        return self._whois_table

    @Plugin.command('whois', '<name:str...>')
    def on_hey_command(self, event, name):
        if name in self.whois_table:
            event.msg.reply(self.whois_table[name])
