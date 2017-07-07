.. _how_to_dev_gridgen:

格子生成プログラムの作成
========================

格子生成プログラムを作成します。この例では、格子生成プログラムは FORTRAN
言語で開発します。

iRIC と連携する格子生成プログラムを開発するには、
格子生成プログラム定義ファイルに従って iRIC
が生成する格子生成データファイルを、
格子生成条件、格子の入出力に利用する必要があります。

iRIC が生成する格子生成データファイルは、CGNS
ファイルという形式です。CGNS ファイルの入出力には、iRIClib
というライブラリを使用します。

この節では、:ref:`how_to_create_gridgen_def_file` 
で作成した定義ファイルに従ってiRIC が生成する格子生成データファイルを読みこんで、
格子を生成するプログラムを開発する流れを説明します。

この格子生成プログラムで行われる入出力処理を :numref:`gridgenerator_dev_flow`
に示します。

.. _gridgenerator_dev_flow:

.. csv-table:: 格子生成プログラムの入出力の処理の流れ
   :file: gridgenerator_dev_flow.csv
   :header-rows: 1


この節では、格子生成プログラムを以下の手順で作成します。

#. 骨組みの作成
#. 格子生成データファイルを開く処理、閉じる処理の記述
#. 格子の出力処理の記述
#. 格子生成条件の読み込み処理の記述
#. エラー処理の記述

.. toctree::
   :maxdepth: 4

   03_01_gridgenerator_skeleton
   03_02_gridgenerator_openclose
   03_03_gridgenerator_add_gridoutput
   03_04_gridgenerator_add_load_cond
   03_05_gridgenerator_add_errorhandling
