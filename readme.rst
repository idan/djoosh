Djoosh 
======

`Djoosh`_ is a reusable django app which provides extensible, pure-python fulltext indexing for Django models using the `Whoosh`_ information-retrieval library. 

The djoosh project lives at http://github.com/idangazit/djoosh/.

.. _Djoosh: http://github.com/idangazit/djoosh/


Project Goals
-------------

Djoosh will:

* be a **pure-python** fulltext indexing solution. There are many fine solutions based around `Lucene`_ and `Solr`_ (java), or `Xapian`_ (C/C++). There is even one solution (`django-search`_) which provides pluggable indexing backends much like the ORM supports various DB backends. This project utilizes `Whoosh`_ exclusively.
* be simple enough to make "**out of the box indexing**" no harder than registering a model for usage in django's admin.
* be **flexible/extensible** enough that you can specify custom indexing behavior for a model if you need it -- much like you can specify a custom form for the admin.
* be as **pythonic, djangonic and KISS** as we can make it. :)

.. _Whoosh: http://trac.whoosh.ca/
.. _Lucene: http://lucene.apache.org/java/docs/
.. _Solr: http://lucene.apache.org/solr/
.. _Xapian: http://xapian.org/
.. _django-search: http://code.google.com/p/djangosearch/

We're consciously trying to ape the architecture and methodology of the django admin in order to reduce brain overhead. We'd like people to pick up djoosh and feel right at home because it looks, works, and smells a lot like the admin.

Project Anti-Goals
------------------

Given our choice of indexing library, this project will not be about raw index/search speed. If you are looking for the fastest possible indexing solution, this probably isn't it.

We're probably not going to grow this into a multi-backend search solution, then again "never say never".

Wishlist
--------

* Once the basic indexing solution is working, maybe include a django application that provides an HTTP interface to a djoosh. This will allow you to separate the djoosh indexing service from the django appserver, and make it available to more than one django server via the network.
* Peace on earth and goodwill towards men.


Architecture
============

This is a big fat TODO. We've captured some ideas on paper and worked out a basic design, we'll fill this one once we've fleshed the project out a bit.


Usage
=====

*See: Architecture.*


Meta
====

License
-------
Djoosh is yours to use, modify, and redistribute according to the terms of the BSD license, the full text of which is in a file named ``LICENSE.txt``, which should be in the same directory as this readme.

Contributors
------------

* Meir Kriheli <meir AT mksoft.co.il>
* Idan Gazit <idan AT pixane.net>
* PyWeb-IL attendees (http://groups.google.com/group/pyweb-il/)

That's a truly stupid name for a project.
-----------------------------------------

So suggest a better one. :)