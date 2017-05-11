.. image:: https://img.shields.io/pypi/v/chucknorris.svg
   :target: https://pypi.org/project/chucknorris

.. image:: https://img.shields.io/pypi/pyversions/chucknorris.svg

.. image:: https://img.shields.io/pypi/dm/chucknorris.svg

.. image:: https://img.shields.io/travis/yougov/chucknorris/master.svg
   :target: http://travis-ci.org/yougov/chucknorris

A library of quips about Chuck Norris, including a plugin for pmxbot to
apply the quips to your chat colleagues.


License
=======

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

Usage
=====

    >>> import chucknorris.quips as q
    >>> q.random('Janet')
    'Janet doesn't wear a watch. She decides what time it is.'


Plugin Setup
============

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
