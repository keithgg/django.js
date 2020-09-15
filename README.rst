=====
NOTES
=====

This is a unmaintained fork of https://github.com/noirbizarre/django.js/

It contains work from https://github.com/pcompassion/django.js commit `79fe23c4c198c922f05f0d01c9ed16c0960a942e` with fixes for Django3 and Py3 compatibility.
Installation
============

Add ``djangojs`` to your ``settings.INSTALLED_APPS``.

Add ``djangojs.urls`` to your root ``URL_CONF``:

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^djangojs/', include('djangojs.urls')),
        ...
    )


Documentation
=============

The documentation is hosted `on Read the Docs <http://djangojs.readthedocs.org/en/latest/>`_
