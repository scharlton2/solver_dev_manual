Initializing iRIClib
========================

Prepares the CGNS file that has been opened for use by iRIClib.
After the CGNS file is opened, this should be executed.

When you add calculation result to the CGNS file,
open the CGNS file with CG_MODE_MODIFY mode, and initialize
using \\"cg_iric_init_f\\".

When you just read grid and calculation result from CGNS file,
open the CGNS file with CG_MODE_READ mode, and initialize using
\\"cg_iric_initread_f\\".

.. list-table:: Subroutine to use
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_init_f
     - Initialize the internal variables that are used for reading and modifying the opened CGNS file.
   * - cg_iric_initread_f
     - Initialize the internal variables that are used for reading the opened CGNS file.
