pronouns = dict(
    male = {
        'his': 'his',
        'he': 'he',
        'He': 'He',
        'His': 'His',
        'him': 'him',
    },
    female = {
        'his': 'her',
        'he': 'she',
        'He': 'She',
        'His': 'Her',
        'him': 'her',
    }
)

female_nicks = set()
male_nicks = set()
default_gender = 'male'

def load_nicks(config):
    female_nicks.update(config.get('female nicks', []))
    male_nicks.update(config.get('male nicks', []))
    globals().update(
        default_gender=config.get('default gender', default_gender))

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
    # default to male because there tends to be more of that going on
    return default_gender


def pronounify(sentence, orig_name, nick=None):
    """
    Replace 'his' and 'he' with 'her' and 'she' if nick is female.  Assume
    sentence uses string formatting like {his} and {he}.
    """
    gender = nick_gender(nick or '')
    if nick:
        sentence = sentence.replace(orig_name, nick)
    return sentence.format(**pronouns[gender])
