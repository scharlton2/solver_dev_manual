計算条件・境界条件・格子生成条件の項目の定義と読み込み処理の例
--------------------------------------------------------------

ソルバー定義ファイルでの計算条件、格子生成プログラムでの格子生成条件の
項目の定義例を示します。定義する位置は
:numref:`where_to_define_element`
に示すように異なりますが、同じ文法で定義できます。各対象ファイルの構造は
:ref: `def_structure` を参照してください。

.. _where_to_define_element:

.. csv-table:: 要素の定義位置
   :file: where_to_define_element.csv
   :header-rows: 1

定義できる項目の種類を、 :numref:`definition_file_widget_types`
に示します。この節では、以下を示します。

- 定義例
- iRIC の計算条件編集ダイアログ上での表示例
- ソルバー (もしくは格子生成プログラム) で値を読み込むための処理の記述例

ソルバー (もしくは格子生成プログラム) で値を読み込むための
処理の記述例では、iRIClib の関数を使用しています。iRIClib
の詳細は、6章を参照して下さい。

記述例は読み込みに関連する部分のみですので、プログラム全体の例は
2.3.4, 4.4を参照してください。

.. _definition_file_widget_types:

.. csv-table:: 計算条件、格子生成条件の項目の種類
   :file: widget_types.csv
   :header-rows: 1

.. toctree::
   :maxdepth: 2

   03_01_01_example_string
   03_01_02_example_filename_read
   03_01_03_example_filename_save
   03_01_04_example_foldername
   03_01_05_example_integer
   03_01_06_example_integer_select
   03_01_07_example_real
   03_01_08_example_func
   03_01_09_example_func_multi
