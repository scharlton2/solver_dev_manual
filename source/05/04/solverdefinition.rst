SolverDefinition
================

SolverDefinition element contains definition information of the solver.

Examples
--------

.. code-block:: xml
   :caption: Example of SolverDefinition definition
   :name: ref_solverdefinition_example
   :linenos:

   <SolverDefinition
     name="samplesolver"
     caption="Sample Solver 1.0"
     version="1.0"
     copyright="Example Company"
     release="2012.04.01"
     homepage="http://example.com/"
     executable="solver.exe"
     iterationtype="time"
     gridtype="structured2d"
   >
     <CalculationCondition>

       (abbr.)

     </CalculationCondition>
     <GridRelatedCondition>

       (abbr.)

     </GridRelatedCondition>
   </SolverDefinition>

Attributes
-----------

.. csv-table:: Attributes of SolverDefinition
   :file: solverdefinition_attributes.csv
   :header-rows: 1

.. csv-table:: iterationtype value
   :file: solverdefinition_att_iterationtype.csv
   :header-rows: 1

.. csv-table:: gridtype value
   :file: solverdefinition_att_gridtype.csv
   :header-rows: 1

When solver developers want to update solvers, version attribute should be changed.
Refer to :ref:`notice_about_version` for notes on solver version up.

Child elements
--------------

.. csv-table:: Child elements of SolverDefinition
   :file: solverdefinition_elements.csv
   :header-rows: 1
