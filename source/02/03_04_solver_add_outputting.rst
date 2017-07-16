.. _solver_dev_add_outputting:


Adding codes to output time and calculation results
----------------------------------------------------

Adds codes to output time and calculation results.

When you develop a solver that is used for time-dependent flow, you have
to repeat outputting time and calculation results for the number of time
steps.

Before starting outputting calculation results, the solver should check
whether user canceled calculation. If canceled, the solver should stop.

In solver definition files, no definition is written about the
calculation results the solver output. So, you do not have to take care
about the correspondence relation between solver definition file and the
solver code about them.

:numref:`solver_with_outputting` shows the source code with
lines to output time and
calculations. The added lines are shown with highlight.

.. code-block:: fortran
   :caption: Source code with lines to output time and calculation results
   :name: solver_with_outputting
   :linenos:
   :emphasize-lines: 6-13,21-49

     ! (abbr.)
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle
     double precision:: time
     integer:: iteration
     integer:: canceled
     integer:: locked
     double precision, dimension(:,:), allocatable:: velocity_x, velocity_y
     double precision, dimension(:,:), allocatable:: depth
     integer, dimension(:,:), allocatable:: wetflag
     double precision:: convergence

     ! (abbr.)

     ! Loads grid attributes 
     call cg_iric_read_grid_real_node_f("Elevation", elevation, ier)
     call cg_iric_read_grid_integer_cell_f("Obstacle", obstacle, ier)

     allocate(velocity_x(isize,jsize), velocity_y(isize,jsize), depth(isize,jsize), wetflag(isize,jsize))
     iteration = 0
     time = 0
     do
       time = time + timestep
       ! (Execute the calculation here. The grid shape changes.)

       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit
       call iric_check_lock_f(condFile, locked)
       do while (locked == 1)
         sleep(1)
         call iric_check_lock_f(condFile, locked)
       end do
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       ! Outputs grid
       call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
       ! Outputs calculation result
       call cg_iric_write_sol_real_f ('VelocityX', velocity_x, ier)
       call cg_iric_write_sol_real_f ('VelocityY', velocity_y, ier)
       call cg_iric_write_sol_real_f ('Depth', depth, ier)
       call cg_iric_write_sol_integer_f ('Wet', wetflag, ier)
       call cg_iric_write_sol_baseiterative_real_f ('Convergence', convergence, ier)
       call cg_iric_flush_f(condFile, fin, ier)
       call iric_write_sol_end_f(condFile, ier)
       iteration = iteration + 1
       if (iteration > maxiterations) exit
     end do
   
     ! Closes calculation data file
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram

Refer to Section 6.3.10 and 6.3.12 for the details of the subroutines to
output time and calculation results. Refer to Section 6.3.11 for the
details of the subroutines to output the grid coordinates in case of
moving grid.

For the calculation results, some special names is named in iRIC. You
should use that name for calculation results used for a certain purpose.
Refer to Section 7.3 for the special names.
