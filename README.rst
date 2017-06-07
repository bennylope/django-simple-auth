==================
Django Simple Auth
==================

:Info: Super simple password protection for limiting public access to pages and
       assets
:Version: 0.2.1
:Author: Ben Lopatin (http://benlopatin.com)

Django Simple Auth is a *secondary* authentication system for protecting any
URLs served by your application from public access. It does not replace your
authentication system. Rather its purpose is to provide very simple
a simple password for non-public information like shared photo galleries.

Installing
==========

First add the application to your Python path. The easiest way is to use
`pip`::

    pip install django-simple-auth

As of version 0.2.0 this is only tested against Django 1.11+ and is probably compatible
with Django 1.10 but this has not been tested.

Configuring
-----------

Make sure you have `django.contrib.auth` installed, and add the `simple_auth`
application to your `INSTALLED_APPS` list::

    INSTALLED_APPS = [
        ...
        'django.contrib.auth',
        'simple_auth',
    ]

Next add `simple_auth.urls` to your project URLs.::

    ...
    url(r'^protect/', include('simple_auth.urls')),

If you want to enable default rule-based limits on your site, install the
`SimpleAuthMiddleware`::

    MIDDLEWARE = [
        ...
        'simple_auth.middleware.SimpleAuthMiddleware',
    ]

By default this will require a password for all URLs except for URLs prefaced
with `/admin/`. These URLs can be overridden using protect and ignore
settings.::

    SIMPLE_AUTH_IGNORE = [
        r'^admin/,
        r'^$',
    ]

    SIMPLE_AUTH_PROTECT = [
        r'^forums/'
        r^blog/',
        r^secret_page.html$',
    ]

If a URL is listed in both the ignore and protect lists the default will be to
protect the URL and simple_auth will emit a warning.

Usage overview
==============

There are two ways to protect pages and assets: view decorators and middleware.

These methods will always allow authenticated users to access the URL.

Middleware
----------

To enable the middleware install the middleware class as described in the
installation section.

Individual views
----------------

Note: not implemented yet.

For function views::

    from simple_auth import simple_auth_required

    @simple_auth_required
    def myview(request):
        ...

For class-based views::

    from simple_auth import SimpleAuthMixin

    class MyView(SimpleAuthMixin, DetailView):
        ...
