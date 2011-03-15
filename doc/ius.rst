``ius``
======================

.. automodule:: ossvt.ius
   
   .. autoclass:: ius_version
      :members:

      Using the ``ossvt.ius_version()`` is extremely easy::
      
         >>> from ossvt.ius import ius_version
         >>> ius_version('php52')
         '5.2.17'
      
      However you may not care about IUS,
      in this case you would write your own function to pull your software versions.
