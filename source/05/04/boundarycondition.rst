BoundaryCondition
==================

BoundaryCondition element contains boundary condition information.

Example
--------

.. code-block:: xml
   :caption: Example of BoundaryCondition definition
   :name: ref_boundarycondition_example
   :linenos:

   <BoundaryCondition name="inflow" caption="In flow" position="node">
     <Item name="discharge" caption="Discharge">
       <Definition valueType="real" default="0" />
     </Item>
   </BoundaryCondition>

Attributes
-----------

.. csv-table:: Attributes of BoundaryCondition
   :file: boundarycondition_attributes.csv
   :header-rows: 1

.. csv-table:: position values
   :file: boundarycondition_att_position.csv
   :header-rows: 1

Child elements
---------------

.. csv-table:: Child elements of BoundaryCondition
   :file: boundarycondition_elements.csv
   :header-rows: 1

