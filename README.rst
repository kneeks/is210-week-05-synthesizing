####################
IS 210 Assignment 05
####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210

Overview
========

In this brief assignment, we'll be using the scope identifier to conditionally
execute code on running the file.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

In this task you'll be using the datetime module to create a function that
returns today's date and also conditionally executes that date if it's run
on the command line.

Specifications
^^^^^^^^^^^^^^

1.  Create a new module named ``task_01.py``

2.  Import the ``datetime`` module

3.  Create a new constant named ``CURDATE`` and assign it a value of
    ``None``

4.  Create a new function named ``get_current_date()`` that doesn't take
    any parameters

    1.  This function should use ``datetime.date.today()`` to return the
        current day as a ``date`` object.

        .. note::

            You can just return that function's output directly. No additional
            processing is needed. We'll cover objects in the future.

5.  Use the scope identification conditional block to identify if this code is
    being run from an imported module or directly on the command line.

    1.  If the module is being run directly on the command line, use your
        ``get_current_date()`` function to assign ``CURDATE`` the value of
        today's date and print ``CURDATE`` to the command line.

.. warning::

    This task does not have 100% unit test coverage. You will have to get the
    scope portion correct on your own.

Examples
^^^^^^^^
.. code:: pycon

    >>> import task_01
    >>> print task_01.CURDATE
    None
    >>> task_01.get_current_date()
    datetime.date(2015, 1, 1)

.. code:: console

    $ python -i task_01.py
    2015-01-01
    >>> CURDATE
    datetime.date(2015, 1, 1)

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ bash runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
