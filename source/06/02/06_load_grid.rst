.. _iriclib_load_grid:

Reading calculation grid
===========================

Reads a calculation grid from the CGNS file. iRIClib offers
subroutines for reading structured grids only.

.. list-table:: Subroutine to use
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_gotogridcoord2d_f
     - Makes preparations for reading a 2D structured grid
   * - cg_iric_getgridcoord2d_f
     - Reads a 2D structured grid
   * - cg_iric_gotogridcoord3d_f
     - Makes preparations for reading a 3D structured grid
   * - cg_iric_getgridcoord3d_f
     - Reads a 3D structured grid
   * - cg_iric_read_grid_integer_node_f
     - Reads the integer attribute values defined for grid nodes
   * - cg_iric_read_grid_real_node_f
     - Reads the double-precision attribute values defined for grid nodes
   * - cg_iric_read_grid_integer_cell_f
     - Reads the integer attribute values defined for cells
   * - cg_iric_read_grid_real_cell_f
     - Reads the double-precision attribute values defined for cells
   * - cg_iric_read_complex_count_f
     - Reads the number of groups of complex type grid attribute
   * - cg_iric_read_complex_integer_f
     - Reads the integer attribute values of complex type grid attribute
   * - cg_iric_read_complex_real_f
     - Reads the double precision attribute values of complex type grid attribute
   * - cg_iric_read_complex_realsingle_f
     - Reads the single precision attribute values of complex type grid attribute
   * - cg_iric_read_complex_string_f
     - Reads the string attribute values of complex type grid attribute
   * - cg_iric_read_complex_functionalsize_f
     - Checks the size of a functional-type attribute of complex type grid attribute
   * - cg_iric_read_complex_functional_f
     - Reads functional attribute data of complex type grid attribute
   * - cg_iric_read_complex_functionalwithname_f
     - Reads functional attribute of complex type grid attribute (with multiple values)
   * - cg_iric_read_complex_functional_realsingle_f
     - Reads functional attribute data of complex type grid attribute
   * - cg_iric_read_grid_complex_node_f
     - Reads the complex attribute values defined at grid nodes
   * - cg_iric_read_grid_complex_cell_f
     - Reads the complex attribute values defined at grid cells
   * - cg_iric_read_grid_functionaltimesize_f
     - Reads the number of values of dimension \"Time\" for functional grid attribute
   * - cg_iric_read_grid_functionaltime_f
     - Reads the values of dimension \"Time\" for functional grid attribute 
   * - cg_iric_read_grid_functionaldimensionsize_f
     - Reads the number of values of dimension for functional grid attribute
   * - cg_iric_read_grid_functionaldimension_integer_f
     - Reads the values of integer dimension for functional grid attribute
   * - cg_iric_read_grid_functionaldimension_real_f
     - Reads the values of double-precision dimension for functional grid attribute
   * - cg_iric_read_grid_functional_integer_node_f
     - Reads the values of functional integer grid attribute with dimension \"Time\" definied at grid nodes.
   * - cg_iric_read_grid_functional_real_node_f
     - Reads the values of functional double-precision grid attribute with dimension \"Time\" definied at grid nodes.
   * - cg_iric_read_grid_functional_integer_cell_f
     - Reads the values of functional integer grid attribute with dimension \"Time\" definied at grid cells.
   * - cg_iric_read_grid_functional_real_cell_f
     - Reads the values of functional double-precision grid attribute with dimension \"Time\" definied at grid cells.

The same subroutines for getting attributes such as cg_iric_read_grid_integer_node_f
can be used both for two-dimensional structured grids and
three-dimensional structured grids.

An example description for reading a two-dimensional structured grid is
shown in :numref:`example_load_two_dimensional_grid`.

.. code-block:: fortran
   :caption: Example of source code to read a grid
   :name: example_load_two_dimensional_grid
   :linenos:

   program Sample3
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, discharge_size, i, j
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle
     integer:: rain_timeid
     integer:: rain_timesize
     double precision, dimension(:), allocatable:: rain_time
     double precision, dimension(:,:), allocatable:: rain
   
     ! Open CGNS file
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Initialize iRIClib
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! Check the grid size
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
   
     ! Allocate memory for loading the grid
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Read the grid into memory
     call cg_iric_getgridcoord2d_f(grid_x, grid_y, ier)
   
     if (ier /=0) STOP "*** No grid data ***"
     ! (Output)
     print *, 'grid x,y: isize, jsize=', isize, jsize
     do i = 1, min(isize,5)
       do j = 1, min(jsize,5)
         print *, ' (',i,',',j,')=(',grid_x(i,j),',',grid_y(i,j),')'
       end do
     end do
   
     ! Allocate memory for elevation attribute values that are defined for grid nodes.
     allocate(elevation(isize, jsize))
     ! Read the attribute values.
     call cg_iric_read_grid_real_node_f('Elevation', elevation, ier)
     print *, 'Elevation: isize, jsize=', isize, jsize
     do i = 1, min(isize,5)
       do j = 1, min(jsize,5)
         print *, ' (',i,',',j,')=(',elevation(i,j),')'
       end do
     end do
   
     ! Allocate memory for the obstacle attribute that is defined for cells. The size is (isize-1) * (jsize-1) since it is cell attribute.
     allocate(obstacle(isize-1, jsize-1))
     ! Read the attribute values in.
     call cg_iric_read_grid_integer_cell_f('Obstacle', obstacle, ier)
     print *, 'Obstacle: isize -1, jsize-1=', isize-1, jsize-1
     do i = 1, min(isize-1,5)
       do j = 1, min(jsize-1,5)
         print *, ' (',i,',',j,')=(',obstacle(i,j),')'
       end do
     end do
     ! Read the number of times for Rain
     call cg_iric_read_grid_functionaltimesize_f('Rain', rain_timesize);
     ! Allocate memory for time values of Rain
     allocate(rain_time(rain_timesize))
   
     ! Allocate memory for the rain attribute that is defined for cells. The size is (isize-1) * (jsize-1) since it is cell attribute.  allocate(rain(isize-1, jsize-1))
     ! Read the attribute at Time = 1
     rain_timeid = 1
     call cg_iric_read_grid_functional_real_cell_f('Rain', rain_timeid, rain, ier)
     print *, 'Rain: isize -1, jsize-1=', isize-1, jsize-1
     do i = 1, min(isize-1,5)
       do j = 1, min(jsize-1,5)
         print *, ' (',i,',',j,')=(',rain(i,j),')'
       end do
     end do
   
     ! Deallocate memory that has been allocated
     deallocate(grid_x, grid_y, elevation, obstacle, rain_time, rain)
   
     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program Sample3

Processing for a three-dimensional grid can be described in the same manner.
