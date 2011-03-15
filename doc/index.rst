.. Open Source Software Version Tracker documentation master file, created by
   sphinx-quickstart on Sat Mar 12 13:06:36 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Open Source Software Version Tracker's documentation!
================================================================

Open Source Software Version Tracker or ``ossvt`` is a set of tools that help you compare your software versions with upstreams.
We use simple ``ConfigObj`` to store upstreams URL and a regular expresion to strip out the latest version number, 
and a simple ``ossvt.ius`` module to parse a rpm repo list. 

If you are building your own tracker you will most likely need to implement a new function in place of the ``ossvt.ius``,
but you can see all this function does is returns your version number.

The official source can be downloaded from https://github.com/jness/ossvt under the terms of the GNU Public License v2

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

