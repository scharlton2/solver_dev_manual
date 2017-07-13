.. _solver_dev_add_open_close:

Adding calculation data file opening and closing codes
-------------------------------------------------------

Adds codes for opening and closing calculation data file.

The solver has to open calculation data file in the first step, and
close it in the last step.

iRIC will handle the file name of calculation data file as a the first
argument, so open that file.

The way to handle the number of arguments and the arguments differs by
compilers. Refer to Section 7.1 for the way to handle them with gfortran
and Intel Fortran Compiler. In this chapter we will add codes that can
be compiled using Intel Fortran Compiler.

Table :numref:`solver_with_open_close` shows the source code with the
lines to open and close calculation data file. The added lines are shown
with highlight.

.. code-block:: fortran
   :caption: The source code with lines to open and close file
   :name: solver_with_open_close
   :linenos:
   :emphasize-lines: 4-6,10-30

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
     integer:: fin, ier
     integer:: icount, istatus
     character(200)::condFile

     write(*,*) "Sample Program"

     icount = nargs()
     if ( icount.eq.2 ) then
       call getarg(1, condFile, istatus)
     else
       write(*,*) "Input File not specified."
       stop
     endif

     ! Opens calculation data file.
     call cg_open_f(condFile, CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"

     ! Initializes iRIClib
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
     ! Set options
     call iric_initoption_f(IRIC_OPTION_CANCEL, ier)
     if (ier /=0) STOP "*** Initialize option error***"

     ! Closes calculation data file.
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram


Compile and deploy the executable file, just like in
:ref:`solver_dev_skeleton`.

Check whether it can be launched from iRIC successfully, just like in
:ref:`solver_dev_skeleton`.

Refer to Section 6.3.2, 6.3.3 and 6.3.13 for the details of the
subroutines added in this section.
