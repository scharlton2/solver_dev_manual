関数型 (複数の値)
-----------------

.. code-block:: xml
   :caption: 関数型 (複数の値) の条件の定義例
   :name: widget_example_func_multi_def
   :linenos:

   <Item name="discharge_and_elev" caption="Discharge and Water Elevation time series">
     <Definition valueType="functional" >
       <Parameter name="time" valueType="real" caption="Time" />
       <Value name="discharge" valueType="real" caption="Discharge" />
       <Value name="elevation" valueType="real" caption="Water Elevation" />
     </Definition>
   </Item>

.. _widget_example_func_multi:

.. figure:: images/widget_example_func_multi.png

   関数型 (複数の値) の条件の表示例

.. code-block:: fortran
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (計算条件・格子生成条件)
   :name: widget_example_func_multi_load_calccond
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: time_value
   double precision, dimension(:), allocatable:: discharge_value, elevation_value

   ! サイズを調べる
   call cg_iric_read_functionalsize_f("discharge", discharge_size, ier)
   ! メモリを確保
   allocate(time_value(discharge_size))
   allocate(discharge_value(discharge_size), elevation_value(discharge_size))
   ! 確保したメモリに値を読み込む
   call cg_iric_read_functionalwithname_f("discharge", "time", time_value)
   call cg_iric_read_functionalwithname_f("discharge", "discharge", discharge_value)
   call cg_iric_read_functionalwithname_f("discharge", "elevation", elevation_value)

.. code-block:: fortran
   :caption: 関数型 (複数の値) の条件を読み込むための処理の記述例 (境界条件)
   :name: widget_example_func_multi_load_bcond
   :linenos:

   integer:: ier, discharge_size
   double precision, dimension(:), allocatable:: time_value
   double precision, dimension(:), allocatable:: discharge_value, elevation_value

   ! サイズを調べる
   call cg_iric_read_bc_functionalsize_f("discharge", discharge_size, ier)
   ! メモリを確保
   allocate(time_value(discharge_size))
   allocate(discharge_value(discharge_size), elevation_value(discharge_size))
   ! 確保したメモリに値を読み込む
   call cg_iric_read_bc_functionalwithname_f("discharge", "time", time_value)
   call cg_iric_read_bc_functionalwithname_f("discharge", "discharge", discharge_value)
   call cg_iric_read_bc_functionalwithname_f("discharge", "elevation", elevation_value)
