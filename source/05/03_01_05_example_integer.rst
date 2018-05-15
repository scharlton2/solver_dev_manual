整数
-----

.. code-block:: xml
   :caption: 整数の条件の定義例
   :name: widget_example_integer_def
   :linenos:

   <Item name="numsteps" caption="The Number of steps to calculate">
     <Definition valueType="integer" default="20" min="1" max="200" />
   </Item>

.. _widget_example_integer:

.. figure:: images/widget_example_integer.png
   :width: 340pt

   整数の条件の表示例

.. code-block:: fortran
   :caption: 整数の条件を読み込むための処理の記述例 (計算条件・格子生成条件)
   :name: widget_example_integer_load_calccond
   :linenos:

   integer:: ier, numsteps

   call cg_iric_read_integer_f("numsteps", numsteps, ier)

.. code-block:: fortran
   :caption: 整数の条件を読み込むための処理の記述例 (境界条件)
   :name: widget_example_integer_load_bcond
   :linenos:

   integer:: ier, numsteps

   call cg_iric_read_bc_integer_f("inflow", 1, "numsteps", numsteps, ier)
