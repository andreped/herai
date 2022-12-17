# herai

💻 Install
-------

    # clone the repository
    $ git clone https://github.com/pallets/flask
    $ cd flask
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above
    $ cd examples/tutorial

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Install Flaskr::

    $ pip install -e .
    
🚀 Run
---

.. code-block:: text

    $ flask --app flaskr init-db
    $ flask --app flaskr --debug run

Open http://127.0.0.1:5000 in a browser.

🔎 Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser
    
⭐ Acknowledgements
----

https://github.com/pallets/flask
