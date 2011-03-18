.. Open Source Software Version Tracker documentation master file, created by
   sphinx-quickstart on Sat Mar 12 13:06:36 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Open Source Software Version Tracker's documentation!
================================================================

Open Source Software Version Tracker or ``ossvt`` is a set of tools that help you compare your software versions with upstreams.
We use simple ``ConfigObj`` to store upstreams URL and a regular expresion to strip out the latest version number, 
and a simple ``ossvt.ius`` module to parse a rpm repo list::

If you are building your own tracker you will most likely need to implement a new function in place of the ``ossvt.ius``,
but you can see all this function does is returns your version number.

The official source can be downloaded from https://github.com/jness/ossvt under the terms of the GNU Public License v2::


   $ ossvt 
   name                           ius ver         upstream ver    status
   ===========================================================================
   mysql50                        5.0.92          5.0.92          up2date
   mysql51                        5.1.56          5.1.56          testing
   mysql55                        5.5.10          5.5.10          testing
   nginx07                        0.7.68          0.7.68          up2date
   php52-eaccelerator             0.9.6.1         0.9.6.1         up2date
   php52-ioncube-loader           3.3.17          4.0.7           outdated
   php52-pear                     1.8.1           1.9.2           outdated
   php52-pecl-apc                 3.1.6           3.1.6           up2date
   php52-pecl-imagick             3.0.1           3.0.1           up2date
   php52-pecl-memcache            3.0.5           3.0.5           up2date
   php52-pecl-xdebug              2.0.5           2.1.0           outdated
   php52-suhosin                  0.9.32.1        0.9.32.1        up2date
   php52-xcache                   1.3.0           1.3.0           up2date
   php52                          5.2.17          5.2.17          up2date
   php53u-eaccelerator            0.9.6.1         0.9.6.1         up2date
   php53u-ioncube-loader          3.3.17          4.0.7           outdated
   php53u-pear                    1.8.1           1.9.2           outdated
   php53u-pecl-apc                3.1.6           3.1.6           up2date
   php53u-pecl-imagick            3.0.1           3.0.1           up2date
   php53u-pecl-memcache           3.0.5           3.0.5           up2date
   php53u-pecl-xdebug             2.0.5           2.1.0           outdated
   php53u-suhosin                 0.9.32.1        0.9.32.1        up2date
   php53u-xcache                  1.3.0           1.3.0           up2date
   php53u                         5.3.5           5.3.6           outdated
   python31-distribute            0.6.6           0.6.15          outdated
   python31-mod_wsgi              3.3             3.3             up2date
   python31-postgresql            1.0.0           1.0.2           outdated
   python31                       3.1.3           3.1.3           testing
   rsyslog4                       4.6.5           4.6.5           up2date

You can even check a single package::

   $ ossvt --name python31
   name                           ius ver         upstream ver    status
   ===========================================================================
   python31                       3.1.3           3.1.3           testing    


Below we have docmentation on each module and its functions:

.. toctree::
   :maxdepth: 2

   upstream
   ius
   ver_compare
   launchpad
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

