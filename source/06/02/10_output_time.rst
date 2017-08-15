Outputting time (or iteration count)
=====================================

Outputs the timestamp information or the iteration count to the CGNS file.

Be sure to perform this before outputting the calculation grid or calculation results.

Also note that the time and iteration-count information cannot be output
at the same time. Output either, not both. 

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_write_sol_time_f
     - Outputs time
   * - cg_iric_write_sol_iteration_f
     - Outputs iteration count

:numref:`example_output_time` shows an example of source code to
output timestamp information.

.. code-block:: fortran
   :caption: Example of source code to output time
   :name: example_output_time
   :linenos:

   program Sample4
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, i
     double precision:: time
   
     ! Open CGNS file.
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Initialize iRIClib.
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! Output the initial state information.
     time = 0
   
     call cg_iric_write_sol_time_f(time, ier)
     ! (Here, output initial calculation grid or calculation results.)
   
     do
       time = time + 10.0
       ! (Perform calculation here.)
       call cg_iric_write_sol_time_f(time, ier)
       ! (Here, output calculation grid or calculation results.)
       If (time > 1000) exit
     end do
   
     ! Close CGNS file.
     call cg_close_f(fin, ier)
     stop
   end program Sample4
