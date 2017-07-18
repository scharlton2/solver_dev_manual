.. _cc_widget_example_func:

Functional
----------

.. code-block:: xml
   :caption: Example of a functional type condition definition
   :name: widget_example_func_def
   :linenos:

   <Item name="discharge" caption="Discharge time series">
     <Definition valueType="functional" >
       <Parameter valueType="real" caption="Time" />
       <Value valueType="real" caption="Discharge" />
     </Definition>
   </Item>

.. _widget_example_func:

.. figure:: images/widget_example_func.png

   Widget example of a functional type condition

.. code-block:: fortran
   :caption: Code example to functional type condition (for calculation conditions and grid generating conditions)
   :name: widget_example_func_load_calccond
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: discharge_time, discharge_value

   ! Read size 
   call cg_iric_read_functionalsize_f("discharge", discharge_size, ier)
   ! Allocate memory
   allocate(discharge_time(discharge_size))
   allocate(discharge_value(discharge_size))
   ! Load values into the allocated memory
   call cg_iric_read_functional_f("discharge", discharge_time, discharge_value, ier)


.. code-block:: fortran
   :caption: Code example to functional type condition (for boundary conditions)
   :name: widget_example_func_load_bcond
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: discharge_time, discharge_value

   ! Read size
   call cg_iric_read_bc_functionalsize_f("inflow", 1, "discharge", discharge_size, ier)
   ! Allocate memory
   allocate(discharge_time(discharge_size))
   allocate(discharge_value(discharge_size))
   ! Load values into the allocated memory
   call cg_iric_read_bc_functional_f("inflow", 1, "discharge", discharge_time, discharge_value, ier)

