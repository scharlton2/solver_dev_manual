BoundaryCondition
==================

境界条件の情報を保持します。

例
----

.. code-block:: xml
   :caption: BoundaryCondition の定義例
   :name: ref_boundarycondition_example
   :linenos:

   <BoundaryCondition name="inflow" caption="In flow" position="node">
     <Item name="discharge" caption="Discharge">
       <Definition valueType="real" default="0" />
     </Item>
   </BoundaryCondition>

属性
-----

.. csv-table:: BoundaryCondition の属性
   :file: boundarycondition_attributes.csv
   :header-rows: 1

.. csv-table:: position の値
   :file: boundarycondition_att_position.csv
   :header-rows: 1

子要素
--------

.. csv-table:: BoundaryCondition の子要素
   :file: boundarycondition_elements.csv
   :header-rows: 1

