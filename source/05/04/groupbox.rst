GroupBox
============

計算条件 (もしくは格子生成条件) の入力ダイアログに表示するグループボックスの定義情報を保持します。

例
----

.. code-block:: xml
   :caption: GroupBox の定義例
   :name: ref_groupbox_example
   :linenos:

   <GroupBox caption="Time">
     <Item name="stime" caption="Start Time">
       <Definition valueType="real" />
     </Item>
     <Item name="etime" caption="End Time">
       <Definition valueType="real" />
     </Item>
   </GroupBox>

GroupBox の定義例は :ref:`layout_groupbox_example` も参照して下さい。

属性
-----

.. csv-table:: GroupBox の属性
   :file: groupbox_attributes.csv
   :header-rows: 1

子要素
--------

.. csv-table:: GroupBox の子要素
   :file: groupbox_elements.csv
   :header-rows: 1
