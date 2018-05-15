.. _calccond_int_select_example:

Integer (Choice)
----------------

.. code-block:: xml
   :caption: Example of a integer (choise) type condition definition
   :name: widget_example_integer_select_def
   :linenos:

   <Item name="flowtype" caption="Flow type">
     <Definition valueType="integer" default="0">
       <Enumeration value="0" caption="Static Flow"/>
       <Enumeration value="1" caption="Dynamic Flow"/>
     </Definition>
   </Item>

.. _widget_example_integer_select:

.. figure:: images/widget_example_combobox.png
   :width: 320pt

   Widget example of a integer (choice) type condition

.. code-block:: fortran
   :caption: Code example to load a integer (choise) type condition (for calculation conditions and grid generating conditions)
   :name: widget_example_integer_select_load_calccond
   :linenos:

   integer:: ier, flowtype

   call cg_iric_read_integer_f("flowtype", flowtype, ier)

.. code-block:: fortran
   :caption: Code example to load a integer (choise) type condition (for boundary conditions)
   :name: widget_example_integer_select_load_bcond
   :linenos:

   integer:: ier, flowtype

   call cg_iric_read_bc_integer_f("inflow", 1, "flowtype", flowtype, ier)
