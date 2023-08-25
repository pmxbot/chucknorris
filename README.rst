.. image:: https://img.shields.io/pypi/v/chucknorris.svg
   :target: https://pypi.org/project/chucknorris

.. image:: https://img.shields.io/pypi/pyversions/chucknorris.svg

.. image:: https://github.com/pmxbot/chucknorris/workflows/tests/badge.svg
   :target: https://github.com/pmxbot/chucknorris/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2023-informational
   :target: https://blog.jaraco.com/skeleton

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
