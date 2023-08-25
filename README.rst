.. image:: https://img.shields.io/pypi/v/chucknorris.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/chucknorris.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/chucknorris

.. image:: https://github.com/pmxbot/chucknorris/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/pmxbot/chucknorris/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

A library of quips about Chuck Norris, including a plugin for pmxbot to
apply the quips to your chat colleagues.


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
