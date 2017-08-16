.. _gridgenerator_dev_skeleton:

Creating a scelton
-------------------

First, create a scelton of a grid generating program. Create a new file
with the source code in :numref:`gridgenerator_skeleton`, and save as
\\"sample.f90\\". At this point, the grid generating program does nothing.

Compile this source code. The way to compile a source code differs by
the compiler. Refer to :ref:`linking_on_ifort` for the procedure to compile using
Intel Fortran Compiler and gfortran.

.. code-block:: fortran
   :caption: Sample grid generating program source code
   :name: gridgenerator_skeleton
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
   end program SampleProgram

Make sure that the compilation succeeds.
