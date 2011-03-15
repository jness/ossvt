``ver_compare``
=========================

.. automodule:: ossvt.ver_compare
   
   .. autoclass:: vcompare
      :members:

      To compare versions we use ``vcompare()`` which is fact pretty simple.

      If our version is up to date the function will return nothing::

         >>> vcompare('5.2.17', '5.2.17')
         >>> 

      But if there is a newer version the function will return that version::

         >>> vcompare('5.2.17', '5.2.19')
         '5.2.19'

      Now that we are familar with all our functions,
      lets bring it all together::

         >>> from ossvt.upstream import package, latest
         >>> from ossvt.ius import ius_version
         >>> from ossvt.ver_compare import vcompare
         >>> for p in pkg:
         ...     upstream = latest(p)
         ...     ius = ius_version(p['name'])
         ...     compare = vcompare(ius, upstream)
         ...     if compare:
         ...             print p['name'], 'outdated'
         ...     else:
         ...             print p['name'], 'up to date'
         ... 
         php52 up to date
