.. _iriclib_load_calccond:

Reading calculation conditions
==============================================

Reads calculation conditions from the CGNS file.

.. list-table:: Subroutines to use
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_read_integer_f
     - Reads an integer calculation-condition value
   * - cg_iric_read_real_f
     - Reads a double-precision real calculation-condition value
   * - cg_iric_read_realsingle_f
     - Reads a single-precision real calculation-condition value
   * - cg_iric_read_string_f
     - Reads a string calculation-condition value
   * - cg_iric_read_functionalsize_f
     - Checks the size of a functional-type calculation condition
   * - cg_iric_read_functional_f
     - Reads functional calculation condition data in double-precision real type
   * - cg_iric_read_functional_realsingle_f
     - Reads functional calculation condition data in single-precision real type
   * - cg_iric_read_functionalwithname_f
     - Reads functional calculation condition data (with multiple values)

For reading calculation condition data other than in functional type,
a subroutine reads a single calculation condition.
An example of reading an integer calculation condition value is 
shown in :numref:`example_load_integer_calccond`.

.. code-block:: fortran
   :caption: Example of source code to read calculation conditions
   :name: example_load_integer_calccond
   :linenos:

   program Sample1
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, i_flow
   
     ! Open CGNS file
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Initialize iRIClib
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     call cg_iric_read_integer_f('i_flow', i_flow, ier)
     print *, i_flow;
   
     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program Sample1
 
In contrast, for getting functional-type calculation conditions,
it is necessary to use two subroutines: cg_iric_read_functionalsize_f
and cg_iric_read_functional_f. An example of getting
functional-type calculation condition data
is shown in :numref:`example_load_functional_calccond`.

.. code-block:: fortran
   :caption: Example of source code to read functional-type calculation conditions
   :name: example_load_functional_calccond
   :linenos:

   program Sample2
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, discharge_size, i
     double precision, dimension(:), allocatable:: discharge_time, discharge_value ! Array for storing discharge time and discharge value
   
     ! Open CGNS file
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! Initialize iRIClib
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! First, check the size of the functional-type input conditions
     call cg_iric_read_functionalsize_f('discharge', discharge_size, ier)
     ! Allocate memory
     allocate(discharge_time(discharge_size), discharge_value(discharge_size))
     ! Read values into the allocated memory
     call cg_iric_read_functional_f('discharge', discharge_time, discharge_value, ier)
   
     ! (Output)
     if (ier ==0) then
       print *, 'discharge: discharge_size=', discharge_size
       do i = 1, min(discharge_size, 5)
         print *, ' i,time,value:', i, discharge_time(i), discharge_value(i)
       end do
     end if
   
     ! Deallocate memory that has been allocated
     deallocate(discharge_time, discharge_value)
   
     ! Close CGNS file
     call cg_close_f(fin, ier)
     stop
   end program Sample2

Refer to :ref:`calccond_def_examples` for examples of codes to load calculation
conditions (or grid generating conditions).
