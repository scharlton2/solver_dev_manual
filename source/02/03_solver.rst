.. _how_to_dev_solver:

ソルバーの作成
==============

ソルバーを作成します。この例では、ソルバーは FORTRAN 言語で開発します。

iRIC と連携するソルバーを開発するには、ソルバー定義ファイルに従って
iRIC が生成する計算データファイルを、計算条件、格子、結果の入出力に
利用する必要があります。

iRIC が生成する計算データファイルは、CGNS ファイルという形式です。
CGNS ファイルの入出力には、iRIClib というライブラリを使用します。

この節では、 :ref:`how_to_create_solver_def_file`
で作成したソルバー定義ファイルに従って iRIC が生成する
計算データファイルを読みこむソルバーを開発する流れを説明します。
このソルバーで行われる入出力処理を :numref:`solver_dev_flow`
に示します。

.. _solver_dev_flow:

.. csv-table:: ソルバーの入出力の処理の流れ
   :file: solver_dev_flow.csv
   :header-rows: 1


この節では、ソルバーを以下の手順で開発していきます。

#. 骨組みの作成
#. 計算データファイルを開く処理、閉じる処理の記述
#. 計算条件、計算格子の読み込み処理の記述
#. 時刻、計算結果の出力処理の記述

.. toctree::
   :maxdepth: 4

   03_01_solver_skeleton
   03_02_solver_openclose
   03_03_solver_add_loading
   03_04_solver_add_outputting
