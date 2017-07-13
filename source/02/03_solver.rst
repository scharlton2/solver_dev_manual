.. _how_to_dev_solver:

Creating a solver
===================

Create a solver. In this example we will develop a solver with FORTRAN.

To develop a solver that works together with iRIC, you have to make it
use calculation data file that iRIC generate, for loading calculation
conditions and grid and outputting calculation results.

The calculation data file that iRIC generates is a CGNS file. You can
use a library called iRIClib to write code for loading and writing CGNS
files.

In this section, the procedure to develop a solver is described,
that load calculation data file, that iRIC generates.
:numref:`solver_dev_flow` shows the input and output processing
that the solver do against the calculation data file.

.. _solver_dev_flow:

.. csv-table:: The I/O processing flow of solver
   :file: solver_dev_flow.csv
   :header-rows: 1

In this section, we will develop a solver in the following procedure:

#. Create a scelton
#. Adds calculation data file opening and closing codes
#. Adds codes to load calculation conditions, calculation girds, and
   boundary conditions
#. Adds codes to output time and calculation results

.. toctree::
   :maxdepth: 4

   03_01_solver_skeleton
   03_02_solver_openclose
   03_03_solver_add_loading
   03_04_solver_add_outputting
