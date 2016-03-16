chucknorris
===========

A library of quips about Chuck Norris, including a plugin for pmxbot to
apply the quips to your chat colleagues.

Plugin Setup
------------

To enable the plugin, just install this package in your pmxbot environment.
Once you've done this, the !norris command will be available. However, due to
the nature of the quips, all chat participants are treated with as the same
gender ('male'). To give your female participants a nicer experience, a
configuration parameter is provided to identify those nicks. Just add a list
of 'female nicks' to your config.yaml::

    female nicks:
      - jen
      - holly
      - judy

And the he/his/him will be replaced with she/her.