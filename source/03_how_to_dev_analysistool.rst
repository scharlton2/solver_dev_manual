Steps of developing a calculation result analysis program
==========================================================

Abstract
--------

Calculation result analysis program is a program that reads calculation
result of a soler from a CGNS file, execute analysis or modify
calculation result. Analysis result or modified calculation results can
be output to another CGNS file.

The steps of developing a calculation result analysis program is
basically the same to that of a solver (See :ref:`how_to_develop_solver`). The difference
is that it handles multiple CGNS files.

To handle multiple CGNS files at the same time, you should use different
functions thant shoes used in :ref:`how_to_develop_solver` (See 6.4.1). 
The names of functions for handling multiple CGNS files ends with
 "\_mul\_f", and the first argument is the file ID. You should call
"cg\_iric\_initread\_f" instead of "cg\_iric\_init\_f" when
initializing the CGNS file to be used by iRIClib.

:numref:`solver_with_multi_cgns` shows the source code to handle
multiple CGNS files.

.. code-block:: fortran
   :caption: Source code that handles multiple CGNS files (abstract)
   :name: solver_with_multi_cgns
   :linenos:


   ! (abbr.)

   ! File opening and initialization
   call cg_open_f(cgnsfile, CG_MODE_MODIFY, fin1, ier)
   call cg_iric_init_f(fin1, ier)

   ! (abbr.)

   ! Reading calculation condition etc.
   call cg_iric_read_functionalsize_mul_f(fin1, 'func', param_func_size, ier)

   ! (abbr.)

   ! File opening and initialization for reading calculation result
   call cg_open_f(param_inputfile, CG_MODE_READ, fin2, ier)
   call cg_iric_initread_f(fin2, ier)

   ! (abbr.)

   ! Reading calculation result etc.
   call cg_iric_read_sol_count_mul_f(fin2, solcount, ier)

   ! (abbr.)

   ! Calculation result analysis code

   ! (abbr.)

   ! Outputting analysis result
   call cg_iric_write_sol_time_mul_f(fin1, t, ier)

   ! (abbr.)

   ! Closing files
   call cg_close_f(fin1, ier)
   call cg_close_f(fin2, ier)

   ! (abbr.)

:numref:`analysis_tool_example_source` shows the source code the
analysis program that reads
calculation result from CGNS file, and executes fish habitat analysis.

.. code-block:: fortran
   :caption: Source code that reads calculation result from CGNS file and output analysis result
   :name: analysis_tool_example_source
   :linenos:

   program SampleProgram2
     implicit none
     include 'cgnslib_f.h'
   
     integer icount
     character(len=300) cgnsfile
   
     integer:: fin1, fin2, ier, istatus
   
     character(len=300) param_inputfile
     integer:: param_result
     character(len=100) param_resultother
     integer:: param_func_size
     double precision, dimension(:), allocatable:: param_func_param
     double precision, dimension(:), allocatable:: param_func_value
     character(len=100) resultname
   
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: target_result
     double precision, dimension(:,:), allocatable:: analysis_result
     double precision:: tmp_target_result
     double precision:: tmp_analysis_result
   
     integer:: i, j, f, solid, solcount, iter
     double precision:: t
   
     ! Code for Intel Fortran
     icount = nargs()
     if (icount.eq.2) then
       call getarg(1, cgnsfile, istatus)
     else
       write(*,*) "Input File not specified."
       stop
     end if
   
     ! Opening CGNS file
     call cg_open_f(cgnsfile, CG_MODE_MODIFY, fin1, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
     ! Initializing internal variables
     call cg_iric_init_f(fin1, ier)
   
     ! Read analysis conditions
     call cg_iric_read_string_mul_f(fin1, 'inputfile', param_inputfile, ier)
     call cg_iric_read_integer_mul_f(fin1, 'result', param_result, ier)
     call cg_iric_read_string_mul_f(fin1, 'resultother', param_resultother, ier)
   
     call cg_iric_read_functionalsize_mul_f(fin1, 'func', param_func_size, ier)
     allocate(param_func_param(param_func_size), param_func_value(param_func_size))
     call cg_iric_read_functional_mul_f(fin1, 'func', param_func_param, param_func_value, ier)
   
     if (param_result .eq. 0) resultname = 'Depth(m)'
     if (param_result .eq. 1) resultname = 'Elevation(m)'
     if (param_result .eq. 2) resultname = param_resultother
   
     ! Read grid from the specified CGNS file
     call cg_open_f(param_inputfile, CG_MODE_READ, fin2, ier)
     if (ier /=0) STOP "*** Open error of CGNS file 2 ***"
     call cg_iric_initread_f(fin2, ier)
     
     ! Reads grid
     call cg_iric_gotogridcoord2d_mul_f(fin2, isize, jsize, ier)
     allocate(grid_x(isize, jsize), grid_y(isize, jsize))
     call cg_iric_getgridcoord2d_mul_f(fin2, grid_x, grid_y, ier)
   
     ! Output the grid to CGNS file
     call cg_iric_writegridcoord2d_mul_f(fin1, isize, jsize, &
       grid_x, grid_y, ier)
   
     ! Allocate memory used for analysis
     allocate(target_result(isize, jsize), analysis_result(isize, jsize))
   
     ! Start analysis of calculation results
     call cg_iric_read_sol_count_mul_f(fin2, solcount, ier)
   
     do solid = 1, solcount
       ! Read calculation result
       call cg_iric_read_sol_time_mul_f(fin2, solid, t, ier)
       call cg_iric_read_sol_real_mul_f(fin2, solid, resultname, &
         target_result, ier)
   
       ! Do fish habitat analysis
       do i = 1, isize
         do j = 1, jsize
           tmp_target_result = target_result(i, j)
           do f = 1, param_func_size
             if ( &
               param_func_param(f) .le. tmp_target_result .and. &
               param_func_param(f + 1) .gt. tmp_target_result) then
               tmp_analysis_result = &
                 param_func_value(f) + &
                 (param_func_value(f + 1) - param_func_value(f)) / &
                 (param_func_param(f + 1) - param_func_param(f)) * &
                 (tmp_target_result - param_func_param(f))
             endif
           end do
           analysis_result(i, j) = tmp_analysis_result
         end do
       end do
   
       ! Output analysis result
       call cg_iric_write_sol_time_mul_f(fin1, t, ier)
       call cg_iric_write_sol_real_mul_f(fin1, 'fish_existence', analysis_result, ier)
     end do
   
     ! Close CGNS files
     call cg_close_f(fin1, ier)
     call cg_close_f(fin2, ier)
     stop
   end program SampleProgram2
