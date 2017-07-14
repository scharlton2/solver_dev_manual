Condition
==========

計算条件 (もしくは格子生成条件) での入力項目が有効になる場合の
条件の情報を保持します。

例
----

.. code-block:: xml
   :caption: Condition の定義例1
   :name: ref_condition_example1
   :linenos:

   <Condition conditionType="isEqual" target="type" value="1" />

.. code-block:: xml
   :caption: Condition の定義例2
   :name: ref_condition_example2
   :linenos:

   <Condition conditionType="and">
     <Condition conditionType="isEqual" target="type" value="1" />
     <Condition conditionType="isEqual" target="inflow" value="0" />
   </Condition>

例は ????? も参照して下さい。

属性
-----

.. csv-table:: Condition の属性
   :file: condition_attributes.csv
   :header-rows: 1

.. csv-table:: conditionType の値
   :file: condition_att_conditiontype.csv
   :header-rows: 1


子要素
--------

.. csv-table:: Condition の子要素
   :file: condition_elements.csv
   :header-rows: 1

