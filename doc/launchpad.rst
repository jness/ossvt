``launchpad``
=======================

.. automodule:: ossvt.launchpad
   
   .. autoclass:: bug_titles
      :members:

      ``ossvt.bug_titles`` uses Launchpad API to get a ``list`` of all Launchpad Bugs on the IUS Community site::

         >>> from ossvt.launchpad import bug_titles
         >>> bug_titles()
         [u'WL: mysql55', u'mysql55: Default my.cnf extremely bare', 
         u'EOL: git17 from IUS (being Added to EPEL)', 
         u'Missing sqlite extension for php53u', 
         u'EOL: python26-ldap from IUS (being Added to EPEL)', 
         ...
         ...
         ]

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
