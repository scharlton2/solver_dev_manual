.. _iriclib_output_grid_in_sol:

Outputting calculation grids (only in the case of a moving grid)
=================================================================

Outputs the calculation grid to the CGNS file.

If the grid shape does not change in the calculation process,
this output is not necessary.

Before outputting the calculation grid at a specific time,
be sure to output the time (or iteration count) information
as described in Section 6.3.10.

The subroutines described in this section should be used for
outputting a calculation grid only when the grid shape is
changed in the course of calculation.
When outputting a grid in the following cases, use the subroutines
described in Section XXXX.

* A new grid has been created in the solver.
* A grid of different number of dimensions or a grid having a
  different grid node count has been created by performing
  re-division of the grid or the like.
* A grid is created in the grid generating program

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_gridcoord2d_f
     - Outputs a two-dimensional structured grid
   * - cg_iric_write_sol_gridcoord3d_f
     - Outputs a three-dimensional structured grid

:numref:`example_output_grid_in_sol` shows an example of outputting
a two-dimensional structured grid after starting calculation.

.. code-block:: fortran
   :caption: Example of source code to output grids after starting calculation
   :name: example_output_grid_in_sol
   :linenos:

   program Sample5
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, isize, jsize
     double precision:: time
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
   
     ! Open CGNS file.
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Initialize iRIClib.
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! Check the grid size.
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
     ! Allocate memory for loading the grid.
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Read the grid into memory.
     call cg_iric_getgridcoord2d_f(grid_x, grid_y, ier)
   
     ! Output the initial state information.
     time = 0
   
     call cg_iric_write_sol_time_f(time, ier)
     ! Output the grid.
     call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
   
     do
       time = time + 10.0
       ! (Perform calculation here.)
       call cg_iric_write_sol_time_f(time, ier)
       call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
       If (time > 1000) exit
     end do
   
     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program Sample5
