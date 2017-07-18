Item
====

計算条件 (もしくは格子生成条件) の入力項目、計算格子の属性、境界条件の定義情報を保持します。

例
----

.. code-block:: xml
   :caption: Item の定義例
   :name: ref_item_example
   :linenos:

   <Item name="stime" caption="Start Time">
     <Definition valueType="real" default="0" />
   </Item>

定義例は :ref:`calccond_def_examples` も参照して下さい。

属性
-----

.. csv-table:: Item の属性
   :file: item_attributes.csv
   :header-rows: 1

子要素
--------

.. csv-table:: Item の子要素
   :file: item_elements.csv
   :header-rows: 1
