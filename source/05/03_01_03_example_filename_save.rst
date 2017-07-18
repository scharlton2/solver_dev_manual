File name (for writing)
------------------------

.. code-block:: xml
   :caption: Example of a file name (for writing) type condition definition
   :name: widget_example_filename_save_def
   :linenos:

   <Item name="flowdatafile" caption="Flow data file">
     <Definition valueType="filename_all" default="flow.dat" />
   </Item>

.. _widget_example_filename_save:

.. figure:: images/widget_example_filename_save.png

   Widget example of a file name type (for writing) condition


.. code-block:: fortran
   :caption: Code example to load a file name (for writing) type condition (for calculation conditions and grid generating conditions)
   :name: widget_example_filename_save_load_calccond
   :linenos:

   integer:: ier
   character(200):: flowdatafile

   call cg_iric_read_string_f("flowdatafile", flowdatafile, ier)

.. code-block:: fortran
   :caption: Code example to load a file name (for writing) type condition (for boundary conditions)
   :name: widget_example_filename_save_load_bcond
   :linenos:

   integer:: ier
   character(200):: flowdatafile

   call cg_iric_read_bc_string_f("inflow", 1, "flowdatafile", flowdatafile, ier)
