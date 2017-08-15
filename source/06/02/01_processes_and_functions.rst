Processes of the program and iRIClib subroutines
========================================================

The I/O processings in solvers and grid generating programs are shown in 
:numref:`processses_of_solver_io` and :numref:`processses_of_gridgenerator_io` .


.. list-table:: I/O processings of solvers
   :name: processses_of_solver_io
   :header-rows: 1

   * - Process
   * - Opens a CGNS file
   * - Initializes iRIClib
   * - Sets up options
   * - Reads calculation conditions
   * - Reads grids
   * - Reads boundary conditions 
   * - Reads geographic data (only when needed)
   * - Outputs grids (only in cases when grid creation or re-division is performed)
   * - Outputs time (or iteration count)
   * - Outputs grids (only in cases when grid moves)
   * - Outputs calculation results
   * - Closes a CGNS file

.. list-table:: I/O processings of a grid generating program
   :name: processses_of_gridgenerator_io
   :header-rows: 1

   * - Process
   * - Opens a CGNS file
   * - Initializes iRIClib 
   * - Reads grid generating condition
   * - Outputs error code
   * - Outputs grid
   * - Closes CGNS File 
