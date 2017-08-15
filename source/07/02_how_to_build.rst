Linking iRIClib, cgnslib using Fortran
===============================================

When you develop solvers (or grid generating programs), you have to link
the program with iRIClib and cgnslib. You have to use different library
files for different compilers like Intel Fortran Compiler and GNU Fortran.
:numref:`library_file_names` shows the files prepared for each compiler.

For header file, \\"libcgns_f.h\\", \\"iriclib_f.h\\" can be used for all
compilers commonly.

.. _library_file_names:

.. list-table:: Files prepared fore each compiler

   * - Compiler
     - iRIClib library
     - cgnslib libraray
   * - Intel Fortran Compiler
     - iriclib_x64_ifort.lib
     - cgnsdll_x64_ifort.lib
   * - GNU Fortran(gfortran)
     - iriclib.lib
     - cgnsdll.lib

We will explain the procedure to compile the source code (solver.f).
We assume that the settings for compilers (like path settings)
are already finished.

Intel Fortran Compiler (Windows)
----------------------------------

Put solver.f, cgnsdll_x64_ifort.lib, iriclib_x64_ifort.lib, cgnslib_f.h, iriclib_f.h
in a same folder, move to that folder with command prompt, and run the following
command to create an executable file named solver.exe.

.. code-block:: batch

   ifort solver.f cgnsdll_x64_ifort.lib iriclib_x64_ifort.lib /MD

When compiling is done, a file named solver.exe.manifest is also created.
When copying the solver to another machine, make sure to copy this file
and to place them together in the same folder.

GNU Fortran
--------------

Put solver.f, cgnsdll.lib, iriclib.lib, cgnslib_f.h, iriclib_f.h in a same folder,
move to that folder with command prompt, and run the following command to
create an executable file named solver.exe.

.. code-block:: batch

   gfortran -c solver.f
   g++ -o solver.exe -lgfortran solver.o cgnsdll.lib iriclib.lib
