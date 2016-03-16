from chucknorris import pronoun
from chucknorris import quips

def setup_module(module):
	config = {
		'female nicks': [
			'tracy',
		],
	}
	pronoun.load_nicks(config)

def test_pronounify():
	assert pronoun.nick_gender('tracy') == 'female'
	assert pronoun.pronounify('James is {his} own best friend', 'James',
		'tracy') == 'tracy is her own best friend'

def test_quips():
	assert 'tracy' in quips.random('tracy')
