.. _gridgenerator_dev_skeleton:

骨組みの作成
------------

格子生成プログラムの骨組みを作成します。
:numref:`gridgenerator_skeleton` に示すソースコードを作成して、
\\"sample.f90\\" という名前で保存します。この時点では、このプログラムは何もしていません。

このソースコードをコンパイルします。コンパイル方法は、コンパイラによって異なります。
gfortran, Intel Fortran Compiler でのコンパイル方法を
:ref:`linking_on_ifort` で解説していますので、参考にしてください。

.. code-block:: fortran
   :caption: サンプル格子生成プログラム ソースコード
   :name: gridgenerator_skeleton
   :linenos:

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
   end program SampleProgram


コンパイルが成功することを確認してください。
