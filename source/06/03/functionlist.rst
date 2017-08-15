List of subroutines
=====================

The table below shows a list of subroutines and their classifications.

.. csv-table:: List of iRIClib subroutines
   :file: funclist.csv
   :header-rows: 1


The functions with \\"O\\" value for column \\"Multi\\" has functions that
are used for the same purpose and used when handling multiple CGNS files.
The \\"Multi\\" version of the functions end with \\"_mul_f\\" instead of \\"_f\\",
and the first argument is file ID.

For example, the functions used for reading integer-type calculation result
are as follows:

* Function used when handling single CGNS file

.. code-block:: fortran

   call cg_iric_read_integer_f(label, intvalue, ier)

* Function used when handling multiple CGNS file.

.. code-block:: fortran

   call cg_iric_read_integer_mul_f(fid, label, intvalue, ier)

The difference between single version and multiple version is shown
in :numref:`difference_single_mul`.
 
.. _difference_single_mul:

.. list-table:: Differences between functions for handling single or mulitple CGNS file
   :header-rows: 1

   * - Item
     - For Single CGNS file
     - For Multiple CGNS file
   * - Name
     - Ends with \\"_f\\"
     - Ends with \\"_mul_f\\"
   * - Arguments
     - See the following sections
     - The first argument is File ID (integer)
   * - Target CGNS file
     - File that is identified by the File ID that was specified as the argument of
       \\"cg_iric_init_f\\" or \\"cg_iric_initread_f\\"
     - File that is identified by the File ID that is specified as the first argument.
