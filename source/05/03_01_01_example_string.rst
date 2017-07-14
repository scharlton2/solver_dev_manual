文字列
------

.. code-block:: xml
   :caption: 文字列の条件の定義例
   :name: widget_example_string_def
   :linenos:

   <Item name="sampleitem" caption="Sample Item">
     <Definition valueType="string" />
   </Item>

.. _widget_example_string:

.. figure:: images/widget_example_string.png

   文字列の条件の表示例


.. code-block:: fortran
   :caption: 文字列の条件を読み込むための処理の記述例 (計算条件・格子生成条件)
   :name: widget_example_string_load_calccond
   :linenos:

   integer:: ier
   character(200):: sampleitem

   call cg_iric_read_string_f("sampleitem", sampleitem, ier)


.. code-block:: fortran
   :caption: 文字列の条件を読み込むための処理の記述例 (境界条件)
   :name: widget_example_string_load_bcond
   :linenos:

   integer:: ier
   character(200):: sampleitem

   call cg_iric_read_bc_string_f("inflow", 1, "sampleitem", sampleitem, ier)
