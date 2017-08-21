.. _create_gridgen_folder:

フォルダの作成
==============

iRIC のインストールフォルダ の下にある \"gridcreators\"
フォルダの下に、開発するソルバーのための専用のフォルダを作成します。今回は、\"example\"
というフォルダを作成します。

.. _how_to_create_gridgen_def_file:

格子生成プログラム定義ファイルの作成
====================================

格子生成プログラム定義ファイルを作成します。

格子生成プログラム定義ファイルは、格子生成プログラムに関する
:numref:`infos_to_define_in_gridgendef` に示す情報を定義します。

.. _infos_to_define_in_gridgendef:

.. csv-table:: 格子生成プログラム定義ファイルで定義する情報
   :file: infos_to_define_in_gridgendef.csv
   :header-rows: 1

定義ファイルは、マークアップ言語の一種であるXML言語で記述します。
XML言語の基礎については :ref:`xml_basics` を参照してください。

この節では、ソルバー定義ファイルを、:numref:`infos_to_define_in_gridgendef`
に示した順で作成していきます。

.. toctree::
   :maxdepth: 4

   02_01_gridgendef_basic
   02_02_gridgendef_gridgencond
   02_03_gridgendef_errorcode
