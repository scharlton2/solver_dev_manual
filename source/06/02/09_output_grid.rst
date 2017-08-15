Outputting calculation grids
==================================

Outputs the calculation grid to the CGNS file.

Unlike ordinary solvers that simply read calculation grids from the CGNS file,
these subroutines are to be used in a particular kind of solver
in which a grid is created on the solver side or
a three-dimensional grid is generated from a two-dimensional grid.

Grid creating program always uses these subroutines.

The subroutines here should be used when a solver output the grid
in the initial state. When you want to output the grid shape 
modified after starting calculation, use the subroutines
described in 6.3.11.

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_writegridcoord1d_f
     - Outputs a one-dimensional structured grid
   * - cg_iric_writegridcoord2d_f
     - Outputs a two-dimensional structured grid
   * - cg_iric_writegridcoord3d_f
     - Outputs a three-dimensional structured grid
   * - cg_iric_write_grid_real_node_f
     - Outputs a grid node attribute with real number value
   * - cg_iric_write_grid_integer_node_f
     - Outputs a grid node attribute with integer value
   * - cg_iric_write_grid_real_cell_f
     - Outputs a grid cell attribute with real number value
   * - cg_iric_write_grid_integer_cell_f
     - Outputs a grid cell attribute with integer value

:numref:`example_export_three_dimensional_grid` shows an example of
the procedure of reading a two-dimensional grid, dividing it to
generate a three-dimensional grid, and then outputting the resulting grid.

.. code-block:: fortran
   :caption: Example of source code to output a grid
   :name: example_export_three_dimensional_grid
   :linenos:

   program Sample7
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, isize, jsize, ksize, i, j, k, aret
     double precision:: time
     double precision:: convergence
     double precision, dimension(:,:), allocatable::grid_x, grid_y, elevation
     double precision, dimension(:,:,:), allocatable::grid3d_x, grid3d_y, grid3d_z
     double precision, dimension(:,:,:), allocatable:: velocity, density
   
     ! Open CGNS file.
     call cg_open_f('test3d.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Initialize iRIClib.
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! Check the grid size.
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
     ! Allocate memory for loading the grid.
     allocate(grid_x(isize,jsize), grid_y(isize,jsize), elevation(isize,jsize))
     ! Read the grid into memory.
     call cg_iric_getgridcoord2d_f(grid_x, grid_y, ier)
     call cg_iric_read_grid_real_node_f('Elevation', elevation, ier)
   
     ! Generate a 3D grid from the 2D grid that has been read in.
     ! To obtain a 3D grid, the grid is divided into 5 __________ with a depth of 5.
   
     ksize = 6
     allocate(grid3d_x(isize,jsize,ksize), grid3d_y(isize,jsize,ksize), grid3d_z(isize,jsize,ksize))
     allocate(velocity(isize,jsize,ksize), STAT = aret)
     print *, aret
     allocate(density(isize,jsize,ksize), STAT = aret)
     print *, aret
     do i = 1, isize
       do j = 1, jsize
         do k = 1, ksize
           grid3d_x(i,j,k) = grid_x(i,j)
           grid3d_y(i,j,k) = grid_y(i,j)
           grid3d_z(i,j,k) = elevation(i,j) + (k - 1)
           velocity(i,j,k) = 0
           density(i,j,k) = 0
         end do
       end do
     end do
     ! Output the generated 3D grid
     call cg_iric_writegridcoord3d_f(isize, jsize, ksize, grid3d_x, grid3d_y, grid3d_z, ier)
   
     ! Output the initial state information
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_time_f(time, ier)
     ! Output the grid.
     call cg_iric_write_sol_gridcoord3d_f(grid3d_x, grid3d_y, grid3d_z, ier)
     ! Output calculation results.
     call cg_iric_write_sol_real_f('Velocity', velocity, ier)
     call cg_iric_write_sol_real_f('Density', density, ier)
     call cg_iric_write_sol_baseiterative_real_f ('Convergence', convergence, ier)
   
   
     do
       time = time + 10.0
       ! (Perform calculation here. The grid shape also changes.)
       call cg_iric_write_sol_time_f(time, ier)
       ! Output the grid.
       call cg_iric_write_sol_gridcoord3d_f(grid3d_x, grid3d_y, grid3d_z, ier)
       ! Output calculation results.
       call cg_iric_write_sol_real_f('Velocity', velocity, ier)
       call cg_iric_write_sol_real_f('Density', density, ier)
       call cg_iric_write_sol_baseiterative_real_f ('Convergence', convergence, ier)
   
       If (time > 100) exit
     end do
   
     ! Close CGNS file.
     call cg_close_f(fin, ier)
     stop
   end program Sample7
