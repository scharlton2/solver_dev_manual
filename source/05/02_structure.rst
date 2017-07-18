.. _def_structure:

Structure
==========

Structures of solver definition files, grid generating program
definition files are described in this section.

Solver definition file
------------------------

Structure of solver definition files for a solver that uses only one
calculation grids is shown in :numref:`def_structure_solverdef`,
and that for a solver that uses
multiple types of calculation grids is shown in
:numref:`def_structure_solverdef_multigridtype`, respectively.

.. _def_structure_solverdef:

.. figure:: images/solverdef_structure_basic.png

   Structure of solver definition file

.. _def_structure_solverdef_multigridtype:

.. figure:: images/solverdef_structure_multigrid.png

   Structure of solver definition files for a solver that uses multiple grid types


When the solver uses multiple types of grids, Solver developers should
add multiple GridType elements, and defines grid structure, grid
attributes, and boundary conditions under each GridType
element.

An example of solver definition file for a solver that uses multiple
grid types, is shown in :numref:`solverdef_example_multigrid`.
In this example, boundary condition
definition is dropped, because that is not required. Please pay
attention that the following point is different:

- Grid structure (gridtype attribute) is not definied in SolverDefinition
  elemenet, but in GridType elements.

When a user creates a new project and selects a solver that bundles the
solver definition shown in :numref:`solverdef_example_multigrid`,
a new pre-processor in :numref:`preprocessor_multigridtypes`
is shown.

.. code-block:: xml
   :caption: An example of solver definition file for a solver that uses multiple types of grids
   :name: solverdef_example_multigrid
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
   <SolverDefinition
     name="multigridsolver"
     caption="Multi Grid Solver"
     version="1.0"
     copyright="Example Company"
     release="2012.04.01"
     homepage="http://example.com/"
     executable="solver.exe"
     iterationtype="time"
   >
     <CalculationCondition>
       <!-- Define calculation conditions here. -->
     </CalculationCondition>
     <GridTypes>
       <GridType name="river" caption="River">
         <GridRelatedCondition>
           <Item name="Elevation" caption="Elevation">
             <Definition valueType="real" position="node" />
           </Item>
           <Item name="Roughness" caption="Roughness">
             <Definition valueType="real" position="node"/>
           </Item>
           <Item name="Obstacle" caption=" Obstacle">
             <Definition valueType="integer" position="cell"/>
           </Item>
         </GridRelatedCondition>
       </GridType>
       <GridType name="floodbed" caption="Flood Bed">
         <GridRelatedCondition>
           <Item name="Elevation" caption="Elevation">
             <Definition valueType="real" position="node" />
           </Item>
         </GridRelatedCondition>
       </GridType>
     </GridTypes>
   </SolverDefinition>

.. _preprocessor_multigridtypes:

.. figure:: images/preprocessor_multigridtypes.png

   Pre-processor image after loading the solver definition file with multiple grid type definitions


Grid generating program definition file
-----------------------------------------

Structure of grid generating program definition file is shown in
:numref:`gridgen_structure`

.. _gridgen_structure:

.. figure:: images/gridgen_structure.png

   Structure of grid generating program definition file
