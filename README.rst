chucknorris
===========

A library of quips about Chuck Norris, including a plugin for pmxbot to
apply the quips to your chat colleagues.

Usage
-----

    >>> import chucknorris.quips as q
    >>> q.random('Janet')
    'Janet doesn't wear a watch. She decides what time it is.'


Plugin Setup
------------

To enable the pmxbot plugin, just install this package in your
pmxbot environment. Once you've done this, the !norris command
will be available.

To override the default gender for a given nickname, just add names
to the relevant nicks in your config.yaml::

    female nicks:
      - beibeix

    male nicks::
      - jaraco

Names like 'judy' or 'brad' will be detected automatically.
