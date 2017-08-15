Special names for grid attributes and calculation results
===========================================================

In iRIC, some special names for grid attribute and calculation results are defined
for certain purposes. Use those names when the solver uses the grid attributes or
calculation results that match the purposes.

Grid attributes
--------------------

:numref:`special_grid_att_names` shows the special names defined for grid attributes.

.. _special_grid_att_names:

.. list-table:: Special names for grid attributes
   :header-rows: 1

   * - Name
     - Description
   * - Elevation
     - Grid attribute that contains elevation of grid nodes (Unit: meter).
       Define \\"Elevation\\" attribute as an attribute defined at grid node,
       with real number type.

When you use \\"Elevation\\" for grid attribute, define an Item element
as a child of GridRelatedCondition element, like :numref:`elevation_def_example`.
You can change caption attribute value to an arbitrary value.


.. code-block:: xml
   :name: elevation_def_example
   :caption: Example of \\"Elevation\\" element definition
   
   <Item name="Elevation" caption="Elevation">
     <Definition position="node" valueType="real" default="max" />
   </Item>

When you create a grid generating program and want to output elevation value,
use name \\"Elevation\\". iRIC will automatically load \\"Elevation\\" value.

:numref:`elevation_output_example` shows an example of code written in Fortran.

.. code-block:: fortran
   :name: elevation_output_example
   :caption: Example of source code to output elevation value in grid generating program

   cg_iric_write_grid_real_node_f("Elevation", elevation, ier);


Calculation results
----------------------

:numref:`special_result_names` shows the special names defined for
calculation results. Specify these names as arguments of subroutines
defined in iRIClib.

:numref:`special_result_output_example` shows an example of solver source code
that outputs all special calculation result.

.. _special_result_names:

.. list-table:: Special names for calculation results

   * - Name
     - Description
     - Required
   * - Elevation
     - Outputs bed elevation (unit: meter). Output the value as real number calculation result. 
       You can add unit in the tail as the part of the name, like \\"Elevation(m)\\".
     - Yes
   * - WaterSurfaceElevation
     - Outputs water surface elevation (unit: meter). Output the value as real number
       calculation result. You can add unit in the tail, like \\"WaterSurfaceElevation(m)\\".
     - 
   * - IBC
     - Valid/invalid flag. At invalid region (i. e. dry region), the value is 0, and at valid region
       (i. e. wet region), the value is 1.
     - 

.. code-block:: fortran
   :name: special_result_output_example
   :caption: Example of source code to output calculation results with the special names

   call cg_iric_write_sol_real_f('Elevation(m)', elevation_values, ier)
   call cg_iric_write_sol_real_f('WaterSurfaceElevation(m)', surface_values, ier)
   call cg_iric_write_sol_integer_f('IBC', IBC_values, ier)
