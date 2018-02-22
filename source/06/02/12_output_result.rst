.. _iriclib_output_result:

Outputting calculation results
==================================

Outputs the calculation results to the CGNS file.

Before outputting the calculation results at a specific time, be sure to output
the time (or iteration count) information as described in :ref:`iriclib_output_time`.

Types of calculation results that can be output with iRIClib are grouped into the followings:

* Calculation results having one value for each time step, without reference to grid nodes
* Calculation results having a value for each grid node

.. list-table:: Subroutines to use for outputting result value that have one value for each time step
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_baseiterative_integer_f
     - Outputs integer-type calculation results
   * - cg_iric_write_sol_baseiterative_real_f
     - Outputs double-precision real-type calculation results

.. list-table:: Subroutines to use for outputting result value that have value at each grid node for each time step
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_integer_f
     - Outputs integer-type calculation results, having a value for each grid node
   * - cg_iric_write_sol_real_f
     - Outputs double-precision real-type calculation results, having a value for each grid node

.. list-table:: Subroutines to use for outputting particles as calculation result for each time step
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_particle_pos2d_f
     - Outputs particle positions (two-dimensions)
   * - cg_iric_write_sol_particle_pos3d_f
     - Outputs particle positions (three-dimensions)
   * - cg_iric_write_sol_particle_integer_f
     - Outputs integer-type calculation results, having a value for each particle
   * - cg_iric_write_sol_particle_real_f
     - Outputs double-precision real-type calculation results, having a value for each particle

.. list-table:: Subroutines to use before and after outputting calculation result for each timestep
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - iric_check_cancel_f
     - Checks whether user canceled solver execution
   * - iric_check_lock_f
     - Checks whether the CGNS file is locked by GUI
   * - iric_write_sol_start_f
     - Inform the GUI that the solver started outputting result
   * - iric_write_sol_end_f
     - Inform the GUI that the solver finished outputting result
   * - cg_iric_flush_f
     - Flush calculation result into CGNS file

:numref:`example_output_calc_result` shows an example of the process to
output calculation results.

.. code-block:: fortran
   :caption: Example of source code to output calculation results
   :name: example_output_calc_result
   :linenos:

   program Sample6
     implicit none
     include 'cgnslib_f.h'

     integer:: fin, ier, isize, jsize
     double precision:: time
     double precision:: convergence
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), allocatable:: velocity_x, velocity_y, depth
     integer, dimension(:,:), allocatable:: wetflag
     double precision, dimension(:), allocatable:: particlex, particley

     ! Open CGNS file
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"

     ! Initialize iRIClib
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"

     ! Check the grid size.
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
     ! Allocate memory for loading the grid.
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Allocate memory for storing calculation results.
     allocate(velocity_x(isize,jsize), velocity_y(isize,jsize), depth(isize, jsize), wetflag(isize,jsize))
     allocate(particlex(10), particley(10))
     ! Read the grid into memory.
     call cg_iric_getgridcoord2d_f (grid_x, grid_y, ier)

     ! Output the initial state information.
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_time_f(time, ier)
     ! Output the grid.
     call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
     ! Output calculation results
     call cg_iric_write_sol_real_f ('VelocityX', velocity_x, ier)
     call cg_iric_write_sol_real_f ('VelocityY', velocity_y, ier)
     call cg_iric_write_sol_real_f ('Depth', depth, ier)
     call cg_iric_write_sol_integer_f ('Wet', wetflag, ier)
     call cg_iric_write_sol_baseiterative_real_f ('Convergence', convergence, ier)
     do
       time = time + 10.0
       ! (Perform calculation here. The grid shape also changes.)
       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit
       call iric_check_lock_f('test.cgn', locked)
       do while (locked == 1)
         sleep(1)
         call iric_check_lock_f(condFile, locked)
       end do
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       ! Output the grid.
       call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
       ! Output calculation results.
       call cg_iric_write_sol_real_f ('VelocityX', velocity_x, ier)
       call cg_iric_write_sol_real_f ('VelocityY', velocity_y, ier)
       call cg_iric_write_sol_real_f ('Depth', depth, ier)
       call cg_iric_write_sol_integer_f ('Wet', wetflag, ier)
       call cg_iric_write_sol_baseiterative_real_f ('Convergence', convergence, ier)
       call cg_iric_write_sol_particle_pos2d_f(10, particlex, particley, ier)
       If (time > 1000) exit
     end do

     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program Sample6


In iRIClib, the same subroutines are used to output vector quantity calculation results and
scalar quantity calculation results. When outputting vector quantity calculation results,
output each component with names like \"VelocityX\" and \"VelocityY\".

For calculation results, iRIC defines special names, and when you want to output
calculation result for certain purposes, you should use those names.
Refer to :ref:`special_result_names` for those names.
