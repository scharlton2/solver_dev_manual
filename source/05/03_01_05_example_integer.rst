Integer
--------

.. code-block:: xml
   :caption: Example of a integer type condition definition
   :name: widget_example_integer_def
   :linenos:

   <Item name="numsteps" caption="The Number of steps to calculate">
     <Definition valueType="integer" default="20" min="1" max="200" />
   </Item>

.. _widget_example_integer:

.. figure:: images/widget_example_integer.png
   :width: 340pt

   Widget example of a integer type condition

.. code-block:: fortran
   :caption: Code example to load a integer type condition (for calculation conditions and grid generating conditions)
   :name: widget_example_integer_load_calccond
   :linenos:

   integer:: ier, numsteps

   call cg_iric_read_integer_f("numsteps", numsteps, ier)

.. code-block:: fortran
   :caption: Code example to load a integer type condition (for boundary conditions)
   :name: widget_example_integer_load_bcond
   :linenos:

   integer:: ier, numsteps

   call cg_iric_read_bc_integer_f("inflow", 1, "numsteps", numsteps, ier)
