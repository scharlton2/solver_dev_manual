Definition (when used under CalculationCondition element or BoundaryCondition element)
=========================================================================================

Definition element contains definition information of calculation
conditions or grid attributes or boundary conditions.

Example
--------

.. code-block:: xml
   :caption: Example of Definition definition 1
   :name: ref_definition_cc_example1
   :linenos:

   <Definition valueType="integer" default="1" />

.. code-block:: xml
   :caption: Example of Definition definition 2
   :name: ref_definition_cc_example2
   :linenos:

   <Definition valueType="integer" default="0" >
     <Enumeration value="0" caption="Standard" />
     <Enumeration value="1" caption="Advanced" />
   </Definition>

Refer to :ref:`calccond_def_examples` for examples of
Condition element definition.

Attributes
-----------

.. csv-table:: Attributes of Definition
   :file: definition_cc_attributes.csv
   :header-rows: 1

.. csv-table:: valueType values
   :file: definition_cc_att_valuetype.csv
   :header-rows: 1


Child elements
--------------

.. csv-table:: Child elements of Definition
   :file: definition_cc_elements.csv
   :header-rows: 1

