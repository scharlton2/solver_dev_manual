Fortran 言語で iriclib, cgnslib とリンクしてビルドする方法
===================================================================

iRIC と連携して動作するソルバー、格子生成プログラムをコンパイルするには、
cgnslib, iriclib とリンクする必要があります。
それぞれ、Intel Fortran Compiler と GNU Fortran では異なるライブラリを利用する
必要があります。それぞれで必要なライブラリのファイル名は
:numref:`library_file_names` のとおりです。
ヘッダファイルは共通で、 \\"libcgns_f.h\\"、 \\"iriclib_f.h\\" です。

.. _library_file_names:

.. list-table::コンパイラ別の、iRIClib, cgnslib 関連のファイル名

   * - コンパイラ
     - iRIClib ライブラリ
     - cgnslib ライブラリ
   * - Intel Fortran Compiler
     - iriclib_x64_ifort.lib
     - cgnsdll_x64_ifort.lib
   * - GNU Fortran(gfortran)
     - iriclib.lib
     - cgnsdll.lib

ソースコードのファイルが solver.f の時のコンパイル手順について以下に示します。
ただし、コンパイラの設定 (pathの設定など) は完了しているものとします。

Intel Fortran Compiler (Windows)
----------------------------------

solver.f, cgnsdll_x64_ifort.lib, iriclib_x64_ifort.lib, cgnslib_f.h, iriclib_f.h
を同じフォルダに置き、そこに移動して以下のコマンドを実行することで、
実行ファイル solver.exe が生成されます。

.. code-block:: Batchfile

   ifort solver.f cgnsdll_x64_ifort.lib iriclib_x64_ifort.lib /MD

コンパイル時には、同時に solver.exe.manifest というファイルも作成されます。
ソルバーをコピーする時はこのファイルも一緒にコピーし、同じフォルダに配置してください。

GNU Fortran
--------------

solver.f, cgnsdll.lib, iriclib.lib, cgnslib_f.h, iriclib_f.h を
同じフォルダに置き、そこに移動して以下のコマンドを実行することで、
実行ファイル solver.exe が生成されます。

.. code-block:: Batchfile

   gfortran -c solver.f
   g++ -o solver.exe -lgfortran solver.o cgnsdll.lib iriclib.lib
