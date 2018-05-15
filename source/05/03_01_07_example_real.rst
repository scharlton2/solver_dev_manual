Real number
------------

.. code-block:: xml
   :caption: Example of a real number type condition definition
   :name: widget_example_real_def
   :linenos:

   <Item name="g" caption="Gravity [m/s2]">
     <Definition valueType="real" default="9.8" />
   </Item>

.. _widget_example_real_select:

.. figure:: images/widget_example_real.png
   :width: 320pt

   Widget example of a real number type condition

.. code-block:: fortran
   :caption: Code example to load a real number type condition (for calculation conditions and grid generating conditions)
   :name: widget_example_real_load_calccond
   :linenos:

   integer:: ier
   double precision:: g

   call cg_iric_read_real_f("g", g, ier)

.. code-block:: fortran
   :caption: Code example to load a real number type condition (for boundary conditions)
   :name: widget_example_real_load_bcond
   :linenos:

   integer:: ier
   double precision:: g

   call cg_iric_read_bc_real_f("inflow", 1, "g", g, ier)

