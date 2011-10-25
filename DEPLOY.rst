======================
Deploying BleachBottle
======================

Deploying BleachBottle is a snap with Gunicorn! It should also work with Apache
and mod_wsgi.


Gunicorn
========

This should get you started::

    $ virtualenv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ gunicorn -w 4 -b 127.0.0.1:5000 bleachbottle:app

That could be automated to run with supervisor or run with ``-D`` to daemonize.


mod_wsgi
========

Make sure the requirements are installed in an environment. You can create one
with ``virtualenv`` and point WSGIPythonHome_ at it. Then point
WSGIScriptAlias_ at ``/path/to/bleachbottle/wsgi.wsgi``.


.. _WSGIPythonHome:
   http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIPythonPath
.. _WSGIScriptAlias:
   http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIScriptAlias
