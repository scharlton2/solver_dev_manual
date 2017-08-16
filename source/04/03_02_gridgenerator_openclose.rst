
格子生成データファイルを開く処理、閉じる処理の記述
--------------------------------------------------

格子生成データファイルを開く処理、閉じる処理を記述します。

格子計算プログラムは、処理開始時に
格子生成データファイルを開き、終了時に閉じる必要があります。iRIC
は引数として格子生成データファイルのファイル名を渡すため、
そのファイル名を開きます。

引数の数と引数を取得するための方法は、コンパイラによって異なります。
Intel Fortran compiler, gfortran での引数の取得方法を
:ref:`handling_arguments` で説明していますので、参考にしてください。
ここでは、Intel Fortran
compiler でコンパイルする場合の方法で記述します。

処理を追記したソースコードを :numref:`gridgenerator_with_open_close`
に示します。追記した部分を強調して示します。

.. code-block:: fortran
   :caption: 計算データファイルを開く処理、閉じる処理を追記したソースコード
   :name: gridgenerator_with_open_close
   :linenos:
   :emphasize-lines: 5-25

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier
     integer:: icount, istatus
   
     character(200)::condFile
   
     icount = nargs()
     if ( icount.eq.2 ) then
       call getarg(1, condFile, istatus)
     else
       stop "Input File not specified."
     endif
   
     ! 格子生成データファイルを開く
     call cg_open_f(condFile, CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! 内部変数の初期化。戻り値は 1 になるが問題ない。
     call cg_iric_init_f(fin, ier)
   
     ! 格子生成データファイルを閉じる
     call cg_close_f(fin, ier)
   end program SampleProgram

:ref:`gridgenerator_dev_skeleton` と同様に、ファイルのコンパイルを行います。
問題なくコンパイルが成功することを確認してください。

この節で追加した関数の詳細については、:ref:`iriclib_open_cgns`,
:ref:`iriclib_init_iriclib`, :ref:`iriclib_close_cgns`
を参照してください。
