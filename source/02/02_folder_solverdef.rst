.. _create_solverdef_folder:

フォルダの作成
==============

iRIC のインストールフォルダ の下にある "solvers"
フォルダの下に、開発するソルバーのための専用のフォルダを作成します。
今回は、 "example" というフォルダを作成します。

.. _how_to_create_solver_def_file:

ソルバー定義ファイルの作成
==========================

ソルバー定義ファイルを作成します。

ソルバー定義ファイルは、ソルバーに関する :numref:`infos_to_define_in_solverdef`
に示す情報を定義します。

.. _infos_to_define_in_solverdef:

.. csv-table:: ソルバー定義ファイルで定義する情報
   :file: infos_to_define_in_solverdef.csv
   :header-rows: 1

ソルバー定義ファイルは、マークアップ言語の一種であるXML言語で記述します。
XML言語の基礎については 5.5 を参照してください。

この節では、ソルバー定義ファイルを、:numref:`infos_to_define_in_solverdef`
に示した順で作成していきます。

.. toctree::
   :maxdepth: 4

   02_01_solverdef_basic
   02_02_solverdef_calccond
   02_03_solverdef_gridcond
   02_04_solverdef_boundarycond
