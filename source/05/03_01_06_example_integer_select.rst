整数 (選択式)
--------------

.. code-block:: xml
   :caption: 整数 (選択式) の条件の定義例
   :name: widget_example_integer_select_def
   :linenos:

   <Item name="flowtype" caption="Flow type">
     <Definition valueType="integer" default="0">
       <Enumeration value="0" caption="Static Flow"/>
       <Enumeration value="1" caption="Dynamic Flow"/>
     </Definition>
   </Item>

.. _widget_example_integer_select:

.. figure:: images/widget_example_combobox.png

   整数 (選択式) の条件の表示例

.. code-block:: fortran
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (計算条件・格子生成条件)
   :name: widget_example_integer_select_load_calccond
   :linenos:

   integer:: ier, flowtype

   call cg_iric_read_integer_f("flowtype", flowtype, ier)

.. code-block:: fortran
   :caption: 整数 (選択式) の条件を読み込むための処理の記述例 (境界条件)
   :name: widget_example_integer_select_load_bcond
   :linenos:

   integer:: ier, flowtype

   call cg_iric_read_bc_integer_f("inflow", 1, "flowtype", flowtype, ier)
