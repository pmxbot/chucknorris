import requests
import cachecontrol.heuristics
import jaraco.functools


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


@jaraco.functools.once
def get_session():
    adapter = cachecontrol.CacheControlAdapter(
        heuristic=cachecontrol.heuristics.ExpiresAfter(days=30))

    sess = requests.Session()
    sess.mount('http://', adapter)
    sess.mount('https://', adapter)
    return sess


def api_lookup(name):
    session = get_session()
    url = 'https://api.genderize.io?name={name}'.format(**locals())
    return session.get(url).json()


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

    return api_lookup(nick)['gender']

def pronounify(sentence, orig_name, nick=None):
    """
    Replace 'his' and 'he' with 'her' and 'she' if nick is female.  Assume
    sentence uses string formatting like {his} and {he}.
    """
    gender = nick_gender(nick or '')
    if nick:
        sentence = sentence.replace(orig_name, nick)
    return sentence.format(**pronouns[gender])
