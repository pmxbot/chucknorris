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

    res = requests.get('https://api.genderize.io?name=' + nick).json()
    return res['gender']

def pronounify(sentence, orig_name, nick=None):
    """
    Replace 'his' and 'he' with 'her' and 'she' if nick is female.  Assume
    sentence uses string formatting like {his} and {he}.
    """
    gender = nick_gender(nick or '')
    if nick:
        sentence = sentence.replace(orig_name, nick)
    return sentence.format(**pronouns[gender])
