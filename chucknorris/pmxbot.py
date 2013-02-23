from __future__ import absolute_import

import pmxbot
from pmxbot.core import command
from pmxbot.karma import Karma

from . import quips
from . import pronoun

@command('norris', aliases=('',),
    doc='Chuck Norris has a website dedicated to pmxbot facts.')
def norrisquote(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return random_quote(rcpt)

def random_quote(nick=None):
    return pronoun.pronounify(quips.random(), 'Chuck Norris', nick)


def init():
    pronoun.load_nicks(pmxbot.config)
