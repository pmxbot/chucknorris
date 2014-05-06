from __future__ import absolute_import

import pmxbot
from pmxbot.core import command
from pmxbot.karma import Karma

from . import quips
from . import pronoun

@command('norris')
def norrisquote(client, event, channel, nick, rest):
    'Chuck Norris has a website dedicated to pmxbot facts.'
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return quips.random(rcpt)

def init():
    pronoun.load_nicks(pmxbot.config)
