import random as _random

import pkg_resources

from . import pronoun

_quips = [quip.rstrip().decode('utf-8') for quip in
    pkg_resources.resource_stream('chucknorris', 'quips.txt')
    if quip.rstrip()]

def random(name=None):
    return pronoun.pronounify(_random.choice(_quips), 'Chuck Norris', name)
