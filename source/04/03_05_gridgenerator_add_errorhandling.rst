.. _gridgenerator_add_errorhandling:

Adding error handling codes
----------------------------

Adds error handling code, to support cases that grid generating
conditions have some problems.

Table:numref:`gridgenerator_with_error_handling` shows
the source code with lines to handle errors. The added
lines are shown with highlight. With the lines added, the grid
generating program will return error when the number of grid nodes
exceeds 100000.

When it is compiled successfully, create a grid with the algorithm in
tha same way to :ref:`gridgenerator_add_groudoutput`.
Check that when you specify big imax and
jmax values, the [Error] dialog (:numref:`gridgenerator_error_dialog`)
will open.

Refer to :ref:`iriclib_output_error` for the subroutines to
output error codes.

.. code-block:: fortran
   :caption: Source code with lines to handle errors
   :name: gridgenerator_with_error_handling
   :linenos:
   :emphasize-lines: 10-16

   ! (abbr.)
   
     ! Loads grid generating condition
     ! To make it simple, no error handling codes are written.
     call cg_iric_read_integer_f("imax", imax, ier)
     call cg_iric_read_integer_f("jmax", jmax, ier)
     call cg_iric_read_integer_f("elev_on", elev_on, ier)
     call cg_iric_read_real_f("elev_value", elev_value, ier)
   
     ! Error handling
     if (imax * jmax > 100000 ) then
       ! It is now possible to create a grid with more than 100000 nodes
       call cg_iric_write_errorcode(1, ier)
       cg_close_f(fin, ier)
       stop
     endif
   
     ! Allocate memory for creating grid
     allocate(grid_x(imax,jmax), grid_y(imax,jmax)
     allocate(elevation(imax,jmax))
   
   ! (abbr.)

.. _gridgenerator_error_dialog:

.. figure:: images/gridgenerator_error_dialog.png

   The [Error] dialog

