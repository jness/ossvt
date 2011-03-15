``launchpad``
=======================

.. automodule:: ossvt.launchpad
   
   .. autoclass:: bug_titles
      :members:

      ``ossvt.bug_titles`` uses Launchpad API to get a ``list`` of all Launchpad Bugs on the IUS Community site::

         >>> from ossvt.launchpad import bug_titles
         >>> bug_titles()
         [u'WL: mysql55', u'mysql55: Default my.cnf extremely bare', u'EOL: git17 from IUS (being Added to EPEL)', u'Missing sqlite extension for php53u', u'EOL: python26-ldap from IUS (being Added to EPEL)', u'WL: ruby 1.9', u'WL: mod_rpaf', u'WL: boost 1.43.0', u'WL: php5x-pecl-memcached', u'WL: subversion16', u'WL: gtk 2.14', u'WL: ImageMagick-6.6.4-2', u'EOL: python26-mysqldb [moved to EPEL]', u'PHP+APC "Unable to allocate memory for pool." error', u'mysqlclient16 required by mysql55 on el6', u'APC 3.1.6 does NOT work with relative path in include()', u'EOL: python26-jsonschema from IUS', u'UPDATE REQUEST mysql51 5.1.56 is available upstream', u'php53 for ius-6', u'UPDATE REQUEST python31 3.1.3 is available upstream']

   .. autoclass:: compare_titles
      :members:
   
      Once we have our titles from ``ossvt.bug_titles()`` we can compare our software name and version, seeing if we already have a bug created.

      Here we are ``returned`` True, this tells us there is already a bug created::
   
         >>> from ossvt.launchpad import bug_titles, compare_titles
         >>> titles = bug_titles()
         >>> compare_titles(titles, 'python31', '3.1.3')
         True

      Now on the other hand we show 3.1.4 does not have a bug created (this may mean we need to created it)::

         >>> from ossvt.launchpad import bug_titles, compare_titles
         >>> titles = bug_titles()
         >>> compare_titles(titles, 'python31', '3.1.4')
         >>> 

   .. autoclass:: create_bug
      :members:
