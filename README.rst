======
jsonui
======
.. External references

.. _PyQT5: https://pypi.org/project/PyQt5/
.. _QScintilla: https://pypi.org/project/QScintilla/
.. _deepdiff: https://pypi.org/project/deepdiff/

.. Internal references

.. _jsonui: https://github.com/barseghyanartur/jsonui/
.. _Read the Docs: http://jsonui.readthedocs.io/
.. _Contributor guidelines: https://fakepy.readthedocs.io/en/latest/contributor_guidelines.html

UI to support JSON.

.. image:: https://img.shields.io/pypi/v/jsonui.svg
   :target: https://pypi.python.org/pypi/jsonui
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/jsonui.svg
    :target: https://pypi.python.org/pypi/jsonui/
    :alt: Supported Python versions

.. image:: https://github.com/barseghyanartur/jsonui/actions/workflows/test.yml/badge.svg?branch=main
   :target: https://github.com/barseghyanartur/jsonui/actions
   :alt: Build Status

.. image:: https://readthedocs.org/projects/jsonui/badge/?version=latest
    :target: http://jsonui.readthedocs.io
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/barseghyanartur/jsonui/#License
   :alt: MIT

.. image:: https://coveralls.io/repos/github/barseghyanartur/jsonui/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/barseghyanartur/jsonui?branch=main
    :alt: Coverage

`jsonui`_ is a UI/GUI tool for working with JSON.

Features
========
- Convert Python dict into JSON.
- Show diffs between two JSONs.

Prerequisites
=============
- Python 3.8+
- `PyQT5`_ (`GPL v3` license)
- `QScintilla`_ (`GPL v3` license)
- `deepdiff`_ (`MIT` license)

Installation
============
pipx
----

.. code-block:: sh

    pipx install jsonui

pip
---

.. code-block:: sh

    pip install jsonui

Documentation
=============
- Documentation is available on `Read the Docs`_.
- For guidelines on contributing check the `Contributor guidelines`_.

Tests
=====

Run the tests with unittest:

.. code-block:: sh

    python -m unittest jsonui

Or pytest:

.. code-block:: sh

    pytest

License
=======

MIT

Support
=======
For security issues contact me at the e-mail given in the `Author`_ section.

For overall issues, go to `GitHub <https://github.com/barseghyanartur/jsonui/issues>`_.

Author
======

Artur Barseghyan <artur.barseghyan@gmail.com>
