.. _special_names:

特別な格子属性、計算結果の名前について
========================================

iRIC では、特別な目的で用いる格子属性、計算結果について、特別な名前を用います。
開発するソルバーで、以下の目的に合致する属性を入出力する場合、ここで示す名前を使ってください。


格子属性
--------

入力格子の属性について定義された特別な名前を :numref:`special_grid_att_names` に示します。

.. _special_grid_att_names:

.. list-table:: 格子属性について定義された特別な名前
   :header-rows: 1

   * - 名前
     - 説明
   * - Elevation
     - 格子点の標高 (単位: m) を保持する格子属性です。格子点の、実数の属性として定義します。

ソルバーで Elevation を使用する場合は、 GridRelatedCondition 要素の子要素の、
Item 要素の name 属性に指定します。caption 属性は任意に設定できます。
定義例を :numref:`elevation_def_example` に示します。

.. code-block:: xml
   :name: elevation_def_example
   :caption: Elevation 要素の定義例
   
   <Item name="Elevation" caption="Elevation">
     <Definition position="node" valueType="real" default="max" />
   </Item>

一方格子生成プログラムで標高情報を出力する場合、 Elevationという名前を使って出力すれば
iRIC で読み込まれます。格子生成プログラムで Elavtion を出力する処理の例を
:numref:`elevation_output_example` に示します。

.. code-block:: fortran
   :name: elevation_output_example
   :caption: 格子生成プログラムでの、Elevation を出力するソースコードの例

   cg_iric_write_grid_real_node_f("Elevation", elevation, ier);

.. _special_result_names:

計算結果
---------

計算結果について定義された特別な名前を
:numref:`special_result_names` に示します。
ここで示す名前は、 iRIClib の関数の引数に指定してください。

これらの特別な計算結果を全て出力するソルバーの例を
:numref:`special_result_output_example` に示します。

.. _special_result_names:

.. list-table:: 計算結果について定義された特別な名前

   * - 名前
     - 説明
     - 必須
   * - Elevation
     - 河床の標高 (単位: m)。実数の計算結果として出力します。\\"Elevation(m)\\" などのように、後ろに単位などの文字列を付加してもかまいません。
     - ○
   * - WaterSurfaceElevation
     - 水面の標高 (単位: m)。実数の計算結果として出力します。\\"WaterSurfaceElevation(m)\\" などのように、後ろに単位などの文字列を付加してもかまいません。
     - 
   * - IBC
     - 計算結果の有効・無効フラグ。無効な (水がない) 領域では 0、有効な (水がある) 領域では 1 を出力します。
     - 

.. code-block:: fortran
   :name: special_result_output_example
   :caption: 特別な名前の計算結果を出力するソースコードの例

   call cg_iric_write_sol_real_f('Elevation(m)', elevation_values, ier)
   call cg_iric_write_sol_real_f('WaterSurfaceElevation(m)', surface_values, ier)
   call cg_iric_write_sol_integer_f('IBC', IBC_values, ier)
