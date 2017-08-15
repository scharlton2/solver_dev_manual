既存の計算結果の読み込み
========================

既存のCGNSファイルに格納されている計算結果を読み込みます。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_read_sol_count_f
     - 計算結果の数を取得する
   * - cg_iric_read_sol_time_f
     - 計算結果の時刻の値を取得する
   * - cg_iric_read_sol_iteration_f
     - 計算結果のループ回数の値を取得する
   * - cg_iric_read_sol_baseiterative_integer_f
     - 整数の計算結果の値を取得する
   * - cg_iric_read_sol_baseiterative_real_f
     - 倍精度実数の計算結果の値を取得する
   * - cg_iric_read_sol_gridcoord2d_f
     - 計算結果の2次元構造格子を取得する
   * - cg_iric_read_sol_gridcoord3d_f
     - 計算結果の3次元構造格子を取得する
   * - cg_iric_read_sol_integer_f
     - 整数の格子点ごとに値を持つ計算結果の値を取得する
   * - cg_iric_read_sol_real_f
     - 倍精度実数の格子点ごとに値を持つ計算結果の値を取得する

既存のCGNSファイルを読み込み、格納されている計算結果を標準出力に
出力する処理の例を :numref:`example_load_calculatioin_result` に示します。


.. code-block:: fortran
   :caption: 計算結果を読み込む処理の記述例
   :name: example_load_calculatioin_result
   :linenos:

   program SampleX
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, isize, jsize, solid, solcount, iter, i, j
     double precision, dimension(:,:), allocatable::grid_x, grid_y, result_real
   
     ! CGNS ファイルのオープン
     call cg_open_f('test.cgn', CG_MODE_READ, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! 内部変数の初期化
     call cg_iric_initread_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! 格子のサイズを調べる
     call cg_iric_gotogridcoord2d_f(isize, jsize, ier)
   
     ! 計算結果を読み込むためのメモリを確保
     allocate(grid_x(isize,jsize), grid_y(isize,jsize))
     allocate(result_real(isize, jsize))
   
     ! 計算結果を読み込み出力
     call cg_iric_read_sol_count_f(solcount, ier)
     do solid = 1, solcount
       call cg_iric_read_sol_iteration_f(solid, iter, ier)
       call cg_iric_read_sol_gridcoord2d_f(solid, grid_x, grid_y, ier)
       call cg_iric_read_sol_real_f(solid, 'result_real', result_real, ier)
   
       print *, 'iteration: ', iter
       print *, 'grid_x, grid_y, result: '
       do i = 1, isize
         do j = 1, jsize
           print *, '(', i, ', ', j, ') = (', grid_x(i, j), ', ', grid_y(i, j), ', ', result_real(i, j), ')'
         end do
       end do
     end do
   
     ! CGNS ファイルのクローズ
     call cg_close_f(fin, ier)
     stop
   end program SampleX


なお、計算結果読み込みの関数を用いて、既存のCGNSファイルの計算結果を
分析・加工することができます（3章参照）。
