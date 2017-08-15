Item
====

Item element contains information that defines an input item of
calculation conditions, grid generating condtions, attributes of the
input grid, or .boundary conditions.

Example
-------

.. code-block:: xml
   :caption: Example of Item definition
   :name: ref_item_example
   :linenos:

   <Item name="stime" caption="Start Time">
     <Definition valueType="real" default="0" />
   </Item>

Refer to :ref:`calccond_def_examples` for examples of Item element definitions.

Attributes
----------

.. csv-table:: Attributes of Item
   :file: item_attributes.csv
   :header-rows: 1

Child elements
----------------

.. csv-table:: Child elements of Item
   :file: item_elements.csv
   :header-rows: 1
