Condition
==========

Condition element contains information of a condition that must be met
when a certain input item of calculation conditions become active.

Example
--------

.. code-block:: xml
   :caption: Example of Condition definition 1
   :name: ref_condition_example1
   :linenos:

   <Condition conditionType="isEqual" target="type" value="1" />

.. code-block:: xml
   :caption: Example of Condition definition 2
   :name: ref_condition_example2
   :linenos:

   <Condition conditionType="and">
     <Condition conditionType="isEqual" target="type" value="1" />
     <Condition conditionType="isEqual" target="inflow" value="0" />
   </Condition>

Refer to ??? for other examples.

Attributes
-----------

.. csv-table:: Attributes of Condition
   :file: condition_attributes.csv
   :header-rows: 1

.. csv-table:: conditionType values
   :file: condition_att_conditiontype.csv
   :header-rows: 1


Child elements
---------------

.. csv-table:: Child elements of Condition
   :file: condition_elements.csv
   :header-rows: 1

