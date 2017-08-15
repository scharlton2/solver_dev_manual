Handling command line arguments in Fortran programs
======================================================

When iRIC launches solvers (or grid generating programs), the name of
calculation data file (or grid generating data file) is passed as
an argument. So, solvers (or grid generating programs) have to process
the file name and opens that file.

In FORTRAN, the functions prepared for handling arguments are
different by compilers. In this section, functions for handling
arguments are explained for Intel Fortran Complier and GNU Fortran compiler.

Intel Fortran Compiler
------------------------

Obtain the number of command line arguments using nargs(),
and obtain the argument value using getarg().

.. code-block:: fortran
   :caption: Example source code for reading arguments for Intel Fortran Compiler
   :linenos:

   icount = nargs()  ! The number includes the executable name, so if user passed one argument, 2 is returned.
   if ( icount.eq.2 ) then
     call getarg(1, condFile, istatus)
   else
     write(*,*) "Input File not specified."
     stop
   endif

GNU Fortran, G95
-----------------

Obtain the number of command line arguments using iargc(),
and obtain the argument value using getarg().

Note that nargs(), getargs() in GNU Fortran has different specification
to those in Intel Fortran Compiler.

.. code-block:: fortran
   :caption: Example source code for reading arguments for GNU Fortran or G95
   :linenos:

   icount = iargc()  ! The number does not includes the executable name, so if user passed one argument, 1 is returned.
   if ( icount.eq.1 ) then
     call getarg(0, str1)      ! The file name of the executable.
     call getarg(1, condfile)  ! The first argument
   else
     write(*,*) "Input File not specified."
     stop
   endif

