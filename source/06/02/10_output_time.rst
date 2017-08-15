.. _iriclib_output_time:

時刻 (もしくはループ回数) の出力
==================================

CGNSファイルに、時刻もしくはループ回数を出力します。

その時刻での計算格子の出力や計算結果の出力を行うより前に、必ず実行してください。

また、時刻とループ回数を両方出力することはできません。必ずいずれかのみ出力してください。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_write_sol_time_f
     - 時刻を出力する
   * - cg_iric_write_sol_iteration_f
     - ループ回数を出力する

時刻を出力する処理の例を :numref:`example_output_time` に示します。

.. code-block:: fortran
   :caption: 時刻を出力する処理の記述例
   :name: example_output_time
   :linenos:

   program Sample4
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, i
     double precision:: time
   
     ! CGNS ファイルのオープン
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! 内部変数の初期化
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! 初期状態の情報を出力
     time = 0
   
     call cg_iric_write_sol_time_f(time, ier)
     ! (ここで、初期の計算格子や計算結果を出力)
   
     do
       time = time + 10.0
       ! (ここで計算を実行)
       call cg_iric_write_sol_time_f(time, ier)
       ! (ここで、計算格子や計算結果を出力)
       If (time > 1000) exit
     end do
   
     ! CGNS ファイルのクローズ
     call cg_close_f(fin, ier)
     stop
   end program Sample4

