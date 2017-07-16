Adding grid generating data file opening and closing codes
-----------------------------------------------------------

Adds codes for opening and closing grid generating data file.

The grid generating program has to open calculation data file in the
first step, and close it in the last step.

iRIC will handle the file name of grid generating data file as the first
argument, so open that file.

The way to handle the number of arguments and the arguments differs by
compilers. Refer to Section 7.1 for the way to handle them with gfortran
and Intel Fortran Compiler. In this chapter we will add codes that can
be compiled using Intel Fortran Compiler.

:numref:`gridgenerator_with_open_close` shows the source code with the
lines to open and close grid
generating data file. The added lines are shown with highlight.

.. code-block:: fortran
   :caption: The source code with lines to open and close file
   :name: gridgenerator_with_open_close
   :linenos:
   :emphasize-lines: 5-25

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier
     integer:: icount, istatus
   
     character(200)::condFile
   
     icount = nargs()
     if ( icount.eq.2 ) then
       call getarg(1, condFile, istatus)
     else
       stop "Input File not specified."
     endif
   
     ! Opens grid generating data file
     call cg_open_f(condFile, CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! Initializes iRIClib. ier will be 1, but that is not a problem.
     call cg_iric_init_f(fin, ier)
   
     ! Closes grid generating data file
     call cg_close_f(fin, ier)
   end program SampleProgram

Compile the executable file, just like in :ref:`gridgenerator_dev_skeleton`.

Check that the source code can be compiled successfully.

Refer to Section 6.3.2, 6.3.3 and 6.3.13 for the details of the
subroutines added in this section.
