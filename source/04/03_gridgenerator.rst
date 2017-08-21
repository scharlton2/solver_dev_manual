.. _how_to_dev_gridgen:

Creating a grid generating program
===================================

Create a grid generating program. In this example we will develop a grid
generating program with FORTRAN.

To develop a grid generating program that works together with iRIC, you
have to make it use grid generating data file that iRIC generate, for
loading grid generation conditions and outputting a grid.

The grid generating data file that iRIC generates is a CGNS file. You
can use a library called iRIClib to write code for loading and writing
CGNS files.

In this section, We\'ll explain the procedure to develop a grid
generating program that load calculation data file, that iRIC generates.

:ref:`how_to_create_gridgen_def_file` shows the input and output
processing that the grid
generating program do against the grid generating data file.

.. _gridgenerator_dev_flow:

.. csv-table:: The I/O processing flow of grid generating program
   :file: gridgenerator_dev_flow.csv
   :header-rows: 1

In this section, we will develop a grid generating program in
the following procedure:

#. Create a scelton
#. Adds grid generating data file opening and closing codes
#. Adds codes to output grid
#. Adds codes to load grid generating conditions
#. Adds codes for error handling

.. toctree::
   :maxdepth: 4

   03_01_gridgenerator_skeleton
   03_02_gridgenerator_openclose
   03_03_gridgenerator_add_gridoutput
   03_04_gridgenerator_add_load_cond
   03_05_gridgenerator_add_errorhandling
