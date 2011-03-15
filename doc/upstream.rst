``upstream``
======================

.. automodule:: ossvt.upstream
   
   .. autoclass:: package
      :members:
      
      The basic syntax for your ``pkg_dir`` config is::

         enabled = True
         name = php52
         url = http://www.php.net/downloads.php
         regex = php-(5.2.[0-9]*).tar.gz     

      And there are optional configuration for POST::

         post_value = previous_os
         post_data = src 

      Using ``package()`` is as simple as calling one of your configuration objects::
      
         >>> from ossvt.upstream import package
         >>> package('php52')
         [ConfigObj({'enabled': 'True', 'name': 'php52', 'url': 'http://www.php.net/downloads.php', 'regex': 'php-(5.2.[0-9]*).tar.gz'})]

 
   .. autoclass:: packages
      :members:
   
      The basic options for the ``pkg_dir`` config is::

         enabled = True
         name = php52
         url = http://www.php.net/downloads.php
         regex = php-(5.2.[0-9]*).tar.gz      
  
      And there are optional configuration for POST::

         post_value = previous_os
         post_data = src 

      Using ``packages()`` is as easy as ``package()``, however here no object is passed. Each config is passed back with in a list::
         
         >>> from ossvt.upstream import packages
         >>> packages()
         [ConfigObj({'enabled': 'True', 'name': 'mysql50', 'url': 'http://dev.mysql.com/downloads/mysql/5.0.html'}),
         ConfigObj({'enabled': 'True', 'name': 'mysql51', 'url': 'http://dev.mysql.com/downloads/mysql/5.1.html'}),
         ...
         ...
         ]

   .. autoclass:: latest
      :members:

      Using the ConfigObj retrieved with ``package()`` or ``packages()`` we can now pull the latest upstream version::

         >>> from ossvt.upstream import package, latest
         >>> pkg = package('php52')
         >>> for p in pkg:
         ...     latest(p)
         ... 
         '5.2.17'
