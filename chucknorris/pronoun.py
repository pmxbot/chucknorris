import logging

try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

import requests


pronouns = dict(
    male={
        'his': 'his',
        'he': 'he',
        'He': 'He',
        'His': 'His',
        'him': 'him',
    },
    female={
        'his': 'her',
        'he': 'she',
        'He': 'She',
        'His': 'Her',
        'him': 'her',
    },
)

pronouns[None] = {
    'his': 'their',
    'he': 'they',
    'He': 'They',
    'His': 'Their',
    'him': 'them',
}

female_nicks = set()
male_nicks = set()

def load_nicks(config):
    female_nicks.update(config.get('female nicks', []))
    male_nicks.update(config.get('male nicks', []))


@lru_cache(maxsize=None)
def api_lookup(name):
    """
    >>> try:
    ...     api_lookup('chuck')
    ... except:
    ...     'male'
    'male'
    >>> try:
    ...     api_lookup('norris')
    ... except:
    ...     'male'
    'male'
    >>> try:
    ...     api_lookup('Chuck Norris') is None
    ... except:
    ...     True
    True
    >>> try:
    ...     api_lookup('#channel')
    ... except:
    ...     None
    """
    url = 'https://api.genderize.io'
    r = requests.get(url, params=dict(name=name))
    # Note: raise on error, so we don't cache invalid results
    r.raise_for_status()
    return r.json().get('gender')


def nick_gender(nick):
    """
    Return the gender of the nick.
    """
    # Split on pipe to account for kristi|lunch
    nick = nick.split('|')[0]
    # Strip off trailing underscores
    nick = nick.rstrip('_')
    nick = nick.lower()
    if nick in female_nicks:
        return 'female'
    if nick in male_nicks:
        return 'male'

    try:
        return api_lookup(nick)
    except Exception:
        logging.warning('genderize.io is down')
        return None


def pronounify(sentence, orig_name, nick=None):
    """
    Replace 'his' and 'he' with 'her' and 'she' if nick is female.  Assume
    sentence uses string formatting like {his} and {he}.
    """
    gender = nick_gender(nick or '')
    if nick:
        sentence = sentence.replace(orig_name, nick)
    return sentence.format(**pronouns[gender])
