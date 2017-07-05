.. _solver_dev_skeleton:

骨組みの作成
------------

まずは、ソルバーの骨組みを作成します。
:numref:`solver_skeleton` に示すソースコードを作成して、
sample.f90 という名前で保存します。この時点では、ソルバーは何もしていません。

このソースコードをコンパイルします。コンパイル方法は、コンパイラによって異なります。
gfortran, Intel Fortran Compiler でのコンパイル方法を7.2.1で解説していますので、
参考にしてください。

.. code-block:: fortran
   :caption: サンプルソルバー ソースコード
   :name: solver_skeleton
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
     include 'iriclib_f.h'

     write(*,*) "Sample Program"
     stop
   end program SampleProgram

コンパイルが成功したら、できた実行プログラムを
:ref:`create_solverdef_folder` で作成したフォルダにコピーし、
名前を :ref:`solverdef_create_basic_info` で executable 属性に指定した名前
(この例なら "solver.exe") に変更してください。
またこの時、ソルバーの実行に必要な DLLも同じフォルダにコピーしてください。

iRIC からソルバーが正しく起動できるか確認します。

"Example Solver" をソルバーに用いるプロジェクトを新しく開始し、
以下の操作を行って下さい。

**メニュー**: 計算(C) --> 実行(R)

ソルバーコンソールが起動され、 :numref:`solverconsole_only_message` に示すように
"Sample Program" という文字列が表示されれば、ソルバーを iRIC から正しく起動できています。

.. _solverconsole_only_message:

.. figure:: images/solverconsole_only_message.png 

   ソルバーコンソール表示例

