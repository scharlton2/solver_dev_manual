.. _gridgenerator_add_groudoutput:

Adding codes to output a grid
------------------------------

Adds codes to output grid.

First, add codes to output a very simple grid, to check whether the
program works together with iRIC successfully.

:numref:`gridgenerator_with_grid_output` shows the
source code with lines to output grid. The added
lines are shown with highlight.

.. code-block:: fortran
   :caption: The source code with lines to output grid
   :name: gridgenerator_with_grid_output
   :linenos:
   :emphasize-lines: 7-8,25-40

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier
     integer:: icount, istatus
     integer:: imax, jmax
     double precision, dimension(:,:), allocatable::grid_x, grid_y
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
   
     imax = 10
     jmax = 10
   
     ! Allocate memory for creating grid
     allocate(grid_x(imax,jmax), grid_y(imax,jmax)
   
     ! Generate grid
     do i = 1, imax
       do j = 1, jmax
         grid_x(i, j) = i
         grid_y(i, j) = j
       end do
     end do
   
     ! Outputs grid
     cg_iric_writegridcoord2d_f(imax, jmax, grid_x, grid_y, ier)
   
     ! Closes grid generating data file.
     call cg_close_f(fin, ier)
   end program SampleProgram

When it was compiled successfully, copy the executable file to the
folder you created in :ref:`create_gridgen_folder`,
and rename it into the name you
specified as [executable] attribute in :ref:`gridgendef_create_basic_info`.
This time, rename
into \"generator.exe\". Copy the DLL files into that folder, that is need
to run the grid generating program.

Now check whether the grid generating program can be launched from iRIC
successfully.

Starts a new project with solver \"Nays2DH\", and select \"Sample Grid
Creator\" as the grid generating algorithm like in
:ref:`gridgendef_create_basic_info`. The
[Grid Creation] dialog (:numref:`gridgen_cond_dialog_for_testing`)
will open.

.. _gridgen_cond_dialog_for_testing:

.. figure:: images/gridgen_cond_dialog_for_testing.png
   :width: 280pt

   The [Grid Creation] dialog

Click on [Create Grid], and a 10 x 10 grid will be created and loaded on
the pre-processing window (:numref:`preprocessor_after_gridgen`).

.. _preprocessor_after_gridgen:

.. figure:: images/preprocessor_after_gridgen.png
   :width: 420pt

   The pre-processing window after creating grid

Refer to :ref:`iriclib_output_grid` for the detail of subroutines to output grids.
Note that in :ref:`iriclib_output_grid` the subroutines to output three-dimensional
grids are listed, but they can not be used in grid generating programs.
In grid generating programs, only subroutines to output two-dimensional
grids can be used.
