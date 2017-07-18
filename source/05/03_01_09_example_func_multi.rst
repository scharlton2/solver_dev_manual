Functional (with multiple values)
---------------------------------

.. code-block:: xml
   :caption: Example of a functional (with multiple values) type condition definition
   :name: widget_example_func_multi_def
   :linenos:

   <Item name="discharge_and_elev" caption="Discharge and Water Elevation time series">
     <Definition valueType="functional" >
       <Parameter name="time" valueType="real" caption="Time" />
       <Value name="discharge" valueType="real" caption="Discharge" />
       <Value name="elevation" valueType="real" caption="Water Elevation" />
     </Definition>
   </Item>

.. _widget_example_func_multi:

.. figure:: images/widget_example_func_multi.png

   Widget example of a functional (with multiple values) type condition (for calculation conditions and grid generating conditions)

.. code-block:: fortran
   :caption: Code example to load a functional (with multiple values) type condition
   :name: widget_example_func_multi_load_calccond
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: time_value
   double precision, dimension(:), allocatable:: discharge_value, elevation_value

   ! Read size
   call cg_iric_read_functionalsize_f("discharge", discharge_size, ier)
   ! Allocate memory
   allocate(time_value(discharge_size))
   allocate(discharge_value(discharge_size), elevation_value(discharge_size))
   ! Load values into allocated memory
   call cg_iric_read_functionalwithname_f("discharge", "time", time_value)
   call cg_iric_read_functionalwithname_f("discharge", "discharge", discharge_value)
   call cg_iric_read_functionalwithname_f("discharge", "elevation", elevation_value)

.. code-block:: fortran
   :caption: Code example to load a functional (with multiple values) type condition (for boundary condition)
   :name: widget_example_func_multi_load_bcond
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: time_value
   double precision, dimension(:), allocatable:: discharge_value, elevation_value

   ! Read size
   call cg_iric_read_bc_functionalsize_f("discharge", discharge_size, ier)
   ! Allocate memory
   allocate(time_value(discharge_size))
   allocate(discharge_value(discharge_size), elevation_value(discharge_size))
   ! Load values into allocated memory
   call cg_iric_read_bc_functionalwithname_f("discharge", "time", time_value)
   call cg_iric_read_bc_functionalwithname_f("discharge", "discharge", discharge_value)
   call cg_iric_read_bc_functionalwithname_f("discharge", "elevation", elevation_value)

