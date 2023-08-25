import contextlib
import random as _random

import importlib_resources as resources

from . import pronoun


def _closing(iter):
    with contextlib.closing(iter):
        yield from iter


_quips = [
    quip.rstrip()
    for quip in _closing(
        resources.files().joinpath('quips.txt').open('r', encoding='utf-8')
    )
    if quip.rstrip()
]


def random(name=None):
    return pronoun.pronounify(_random.choice(_quips), 'Chuck Norris', name)
