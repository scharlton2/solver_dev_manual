Definition (計算条件・境界条件・格子生成条件の定義)
===============================================================

計算条件・境界条件・格子生成条件の定義情報を保持します。

例
----

.. code-block:: xml
   :caption: Definition の定義例1
   :name: ref_definition_cc_example1
   :linenos:

   <Definition valueType="integer" default="1" />

.. code-block:: xml
   :caption: Definition の定義例2
   :name: ref_definition_cc_example2
   :linenos:

   <Definition valueType="integer" default="0" >
     <Enumeration value="0" caption="Standard" />
     <Enumeration value="1" caption="Advanced" />
   </Definition>

例は :ref:`calccond_def_examples` も参照して下さい。

属性
-----

.. csv-table:: Definition の属性
   :file: definition_cc_attributes.csv
   :header-rows: 1

.. csv-table:: valueType の値
   :file: definition_cc_att_valuetype.csv
   :header-rows: 1


子要素
--------

.. csv-table:: Definition の子要素
   :file: definition_cc_elements.csv
   :header-rows: 1

