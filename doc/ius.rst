``ius``
======================

.. automodule:: ossvt.ius
   
   .. autoclass:: ius_stable
      :members:

      Using the ``ossvt.ius_version()`` is extremely easy::
      
         >>> from ossvt.ius import ius_stable
         >>> ius_stable('php52')
         '5.2.17'
     
   .. autoclass:: ius_testing
      :members:

      If you package appears out of date in ``ius_stable()``,
      it may be worth to use the IUS Testing channel with ``ius_testing()``
 
         >>> from ossvt.ius import ius_testing
         >>> ius_testing('mysql55')
         '5.5.10'

      However you may not care about IUS,
      in this case you would write your own function to pull your software versions.
