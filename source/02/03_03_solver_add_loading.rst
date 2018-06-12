.. _solver_dev_add_loading:

Adding codes to load calculation conditions, calculation grids, and boundary conditions
----------------------------------------------------------------------------------------

Adds codes to load calculation conditions, calculation girds, and
boundary conditions.

iRIC will output calculation conditions, grids, grid attributes, and
boundary condition according to the solver definition file that
you\'ve created in :ref:`how_to_create_solver_def_file`.
So, the solver has to load them to coincide with the description
in the solver definition file.

:numref:`solver_with_loading` shows the source code with lines
to load calculation condition, grid and boundary condition.
The added lines are shown with highlight.

.. code-block:: fortran
   :caption: The source code with lines to load calculation condition, grid and boundary condition
   :name: solver_with_loading
   :linenos:
   :emphasize-lines: 8-32,34-106

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
     include 'iriclib_f.h'
     integer:: fin, ier
     integer:: icount, istatus
     character(200)::condFile
     integer:: maxiterations
     double precision:: timestep
     integer:: surfacetype
     double precision:: constantsurface
     integer:: variable_surface_size
     double precision, dimension(:), allocatable:: variable_surface_time
     double precision, dimension(:), allocatable:: variable_surface_elevation

     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle

     integer:: inflowid
     integer:: inflow_count
     integer:: inflow_element_max
     integer:: discharge_variable_sizemax
     integer, dimension(:), allocatable:: inflow_element_count
     integer, dimension(:,:,:), allocatable:: inflow_element
     integer, dimension(:), allocatable:: discharge_type
     double precision, dimension(:), allocatable:: discharge_constant
     integer, dimension(:), allocatable:: discharge_variable_size
     double precision, dimension(:,:), allocatable:: discharge_variable_time
     double precision, dimension(:,:), allocatable:: discharge_variable_value

     write(*,*) "Sample Program"

     ! (abbr)

     ! Initializes iRIClib
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
     ! Set options
     call iric_initoption_f(IRIC_OPTION_CANCEL, ier)
     if (ier /=0) STOP "*** Initialize option error***"

     ! Loads calculation condition
     call cg_iric_read_integer_f("maxIteretions", maxiterations, ier)
     call cg_iric_read_real_f("timeStep", timestep, ier)
     call cg_iric_read_integer_f("surfaceType", surfacetype, ier)
     call cg_iric_read_real_f("constantSurface", constantsurface, ier)

     call cg_iric_read_functionalsize_f("variableSurface", variable_surface_size, ier)
     allocate(variable_surface_time(variable_surface_size))
     allocate(variable_surface_elevation(variable_surface_size))
     call cg_iric_read_functional_f("variableSurface", variable_surface_time, variable_surface_elevation, ier)

     ! Check the grid size
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)

     ! Allocate the memory to read grid coordinates
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! Loads grid coordinates
     call cg_iric_getgridcoord2d_f(grid_x, grid_y, ier)

     ! Allocate the memory to load grid attributes defined at grid nodes and grid cells
     allocate(elevation(isize, jsize))
     allocate(obstacle(isize - 1, jsize - 1))

     ! Loads grid attributes
     call cg_iric_read_grid_real_node_f("Elevation", elevation, ier)
     call cg_iric_read_grid_integer_cell_f("Obstacle", obstacle, ier)

     ! Allocate memory to load boundary conditions (inflow)
     allocate(inflow_element_count(inflow_count))
     allocate(discharge_type(inflow_count), discharge_constant(inflow_count))
     allocate(discharge_variable_size(inflow_count))

     ! Check the number of grid nodes assigned as inflow, and the size of time-dependent discharge.
     inflow_element_max = 0
     do inflowid = 1, inflow_count
       ! Read the number of grid nodes assigned as inflow
       call cg_iric_read_bc_indicessize_f('inflow', inflowid, inflow_element_count(inflowid))
       if (inflow_element_max < inflow_element_count(inflowid)) then
         inflow_element_max = inflow_element_count(inflowid)
       end if
       ! Read the size of time-dependent discharge
       call cg_iric_read_bc_functionalsize_f('inflow', inflowid, 'FunctionalDischarge', discharge_variable_size(inflowid), ier);
       if (discharge_variable_sizemax < discharge_variable_size(inflowid)) then
         discharge_variable_sizemax = discharge_variable_size(inflowid)
       end if
     end do

     ! Allocate the memory to load grid nodes assigned as inflow, and time-dependent discharge.
     allocate(inflow_element(inflow_count, 2, inflow_element_max))
     allocate(discharge_variable_time(inflow_count, discharge_variable_sizemax))
     allocate(discharge_variable_value(inflow_count, discharge_variable_sizemax))

     ! Loads boundary condition
     do inflowid = 1, inflow_count
       ! Loads the grid nodes assigned as inflow
       call cg_iric_read_bc_indices_f('inflow', inflowid, inflow_element(inflowid:inflowid,:,:), ier)
       ! Loads the inflow type (0 = constant, 1 = time-dependent)
       call cg_iric_read_bc_integer_f('inflow', inflowid, 'Type', discharge_type(inflowid:inflowid), ier)
       ! Loads the discharge (constant)
       call cg_iric_read_bc_real_f('inflow', inflowid, 'ConstantDischarge', discharge_constant(inflowid:inflowid), ier)
       ! Loads the discharge (time-dependent)
       call cg_iric_read_bc_functional_f('inflow', inflowid, 'FunctionalDischarge', discharge_variable_time(inflowid:inflowid,:), discharge_variable_value(inflowid:inflowid,:), ier)
     end do

     ! Closes the calculation data file
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram

Note that the arguments passed to load calculation conditions, grid
attributes and boundary conditions are the same to the [name] attributes
of Items defined in 
:ref:`solverdef_define_calccond`, :ref:`solverdef_define_gridcond`.

Refer to :ref:`calccond_def_examples` for the relationship between
definitions of calculation condition, grid attributes,
boundary conditions and the iRIClib
subroutines to load them.

Refer to :ref:`iriclib_load_calccond`, 
:ref:`iriclib_load_grid` and :ref:`iriclib_load_bc` for the detail of
subroutines to load calculation condition, grids, and boundary conditions.
