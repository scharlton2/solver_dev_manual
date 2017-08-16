.. _solver_dev_add_open_close:

計算データファイルを開く処理、閉じる処理の記述
----------------------------------------------

計算データファイルを開く処理、閉じる処理を記述します。

ソルバーは、処理開始時に計算データファイルを開き、終了時に計算データファイルを
閉じる必要があります。

iRIC は引数として計算データファイルのファイル名を渡すため、
そのファイルを開きます。

引数の数と引数を取得するための方法は、コンパイラによって異なります。
Intel Fortran Compiler, gfortran
での引数の取得方法を :ref:`handling_arguments`
で説明していますので、参考にしてください。
ここでは、Intel Fortran Compiler でコンパイルする場合の方法で記述します。

計算データファイルを開く処理と閉じる処理を追記したソースコードを
:numref:`solver_with_open_close`
に示します。強調して示したのが追記した部分です。

.. code-block:: fortran
   :caption: 計算データファイルを開く処理、閉じる処理を追記したソースコード
   :name: solver_with_open_close
   :linenos:
   :emphasize-lines: 4-6,10-30

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
     integer:: fin, ier
     integer:: icount, istatus
     character(200)::condFile

     write(*,*) "Sample Program"

     icount = nargs()
     if ( icount.eq.2 ) then
       call getarg(1, condFile, istatus)
     else
       write(*,*) "Input File not specified."
       stop
     endif

     ! 計算データファイルを開く
     call cg_open_f(condFile, CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"

     ! 内部変数の初期化
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
     ! オプションの設定
     call iric_initoption_f(IRIC_OPTION_CANCEL, ier)
     if (ier /=0) STOP "*** Initialize option error***"

     ! 計算データファイルを閉じる
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram

:ref:`solver_dev_skeleton` と同様に、ファイルのコンパイルと、
実行プログラムの配置を行います。

:ref:`solver_dev_skeleton` と同様の手順で、iRIC からソルバーが正しく起動できるか
確認します。エラーメッセージが表示されずに終了すれば成功です。

この節で追加した関数の詳細については、
:ref:`iriclib_open_cgns`, :ref:`iriclib_init_iriclib`, :ref:`iriclib_close_cgns`
を参照してください。
