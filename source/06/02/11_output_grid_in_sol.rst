.. _iriclib_output_grid_in_sol:

計算格子の出力 (計算開始後の格子)
===================================

CGNSファイルに、計算開始後の計算格子を出力します。計算中に格子形状が
変化するソルバーでのみ行います。

特定の時間での計算格子を出力する前に、必ず 6.3.10 で示した時刻
(もしくはループ回数) の出力を行ってください。

以下に示す場合の格子の出力については、6.3.8 で示した関数を利用してください。

* ソルバーで新たに格子を生成した
* ソルバーで格子を再分割するなどして、次元や格子点数が異なる格子を生成した
* 格子生成プログラム内で格子を生成した

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_write_sol_gridcoord2d_f
     - 2次元構造格子を出力する
   * - cg_iric_write_sol_gridcoord3d_f
     - 3次元構造格子を出力する

2次元構造格子を出力する処理の例を :numref:`example_output_grid_in_sol` に示します。

表 6 11 2次元構造格子を出力する処理の記述例

.. code-block:: fortran
   :caption: 2次元構造格子を出力する処理の記述例
   :name: example_output_grid_in_sol
   :linenos:

   program Sample5
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, isize, jsize
     double precision:: time
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
   
     ! CGNS ファイルのオープン
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! 内部変数の初期化
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! 格子のサイズを調べる
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
     ! 格子を読み込むためのメモリを確保
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     ! 格子を読み込む
     call cg_iric_getgridcoord2d_f(grid_x, grid_y, ier)
   
     ! 初期状態の情報を出力
     time = 0
   
     call cg_iric_write_sol_time_f(time, ier)
     ! 格子を出力
     call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
   
     do
       time = time + 10.0
       ! (ここで計算を実行)
       call cg_iric_write_sol_time_f(time, ier)
       call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
       If (time > 1000) exit
     end do
   
     ! CGNS ファイルのクローズ
     call cg_close_f(fin, ier)
     stop
   end program Sample5

