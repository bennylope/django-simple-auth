============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps and credit will always be given.

Please *do* read through this first before you start contributing code. The
Feature Scope section will be of particular interest to those looking to expand
on this app's functionality, and the Pull Request Guidelines explain how I add
code contributions.

Types of Contributions
======================

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/bennylope/django-simple-auths/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Python version
* Django version
* Django-simple-auth version
* Any additional details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

django-simple-auths could always use more documentation, whether as part of the
official django-simple-auths docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/bennylope/django-simple-auths/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome

Get Started!
------------

Ready to contribute? Here's how to set up `django-simple-auths` for local development.

1. Fork the `django-simple-auths` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/django-simple-auths.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv django-simple-auths
    $ cd django-simple-auths/
    $ pip install -r requirements-dev.txt

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
=======================

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst. Any new functionality should align with
   the project goals (see README).
3. The pull request should work for Python 2.6, 2.7, and 3.3, and for PyPy. Check
   https://travis-ci.org/bennylope/django-simple-auths/pull_requests
   and make sure that the tests pass for all supported Python versions.
4. The pull request must also work with Django 1.4-1.7.
5. Please try to follow `Django coding style
   <https://docs.djangoproject.com/en/1.7/internals/contributing/writing-code/coding-style/>`_.
6. Pull requests should include an amount of code and commits that are
   reasonable to review, are **logically grouped**, and based off clean feature
   branches. Commits should be identifiable to the original author by
   name/username and email.

In a nutshell, changes must not break compatability with older installed
versions of the software. You should be able to upgrade an installed version of
Django simple auth by doing nothing more than upgrading the package and
running South's `migration` command.

I am aiming to support each major Django version for `as long as it is
supported
<https://docs.djangoproject.com/en/dev/internals/release-process/#lts-releases>`_.
