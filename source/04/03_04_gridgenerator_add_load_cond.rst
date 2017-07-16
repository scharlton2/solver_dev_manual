Adding codes to load grid generating condition
------------------------------------------------

Adds codes to load grid generating conditions.

iRIC will output grid generating conditions according to the grid
generating program definition file. So, the grid generating program have
to load them to coincide with the description in the grid generating
program definition file.

:numref:`gridgenerator_with_grid_loadgridgencond` shows
the source code with lines to load grid generating
condition. The added lines are shown with highlight. Note that the
arguments passed to load grid generating conditions are the same to the
[name] attributes of Items defined in :ref:`gridgendef_define_gridgencond`.

When it is compiled successfully, create a grid from iRIC in the
procedure same to :ref:`gridgenerator_add_groudoutput`, and
the grid will be created with the condition you specified on
[Grid Creation] dialog.

Refer to 5.3.1 for the relation between definitions of grid generating
condition and the iRIClib subroutines to load them. Refer to 6.3.5 for
the detail of subroutines to load grid generating conditions.

.. code-block:: fortran
   :caption: Source codewith lines to load grid generating conditions
   :name: gridgenerator_with_grid_loadgridgencond
   :linenos:
   :emphasize-lines: 8-9,11,29-34,38,45,51-53

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier
     integer:: icount, istatus
     integer:: imax, jmax
     integer:: elev_on
     double precision:: elev_value
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), elevation
   
     character(200)::condFile
   
     icount = nargs()
     if ( icount.eq.2 ) then
       call getarg(1, condFile, istatus)
     else
       stop "Input File not specified."
     endif
   
     ! Opens grid generating data file.
     call cg_open_f(condFile, CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! Initializes iRIClib. ier will be 1, but that is not a problem.
     call cg_iric_init_f(fin, ier)
   
     ! Loads grid generating condition
     ! To make it simple, no error handling codes are written.
     call cg_iric_read_integer_f("imax", imax, ier)
     call cg_iric_read_integer_f("jmax", jmax, ier)
     call cg_iric_read_integer_f("elev_on", elev_on, ier)
     call cg_iric_read_real_f("elev_value", elev_value, ier)
   
     ! Allocate memory for creating grid
     allocate(grid_x(imax,jmax), grid_y(imax,jmax)
     allocate(elevation(imax,jmax))
   
     ! Generate grid
     do i = 1, isize
       do j = 1, jsize
         grid_x(i, j) = i
         grid_y(i, j) = j
         elevation(i, j) = elev_value
       end do
     end do
   
     ! Outputs grid 
     cg_iric_writegridcoord2d_f(imax, jmax, grid_x, grid_y, ier)
     if (elev_on == 1) then
       cg_iric_write_grid_real_node_f("Elevation", elevation, ier);
     end if
   
     ! Closes grid generating data file.
     call cg_close_f(fin, ier)
   end program SampleProgram
