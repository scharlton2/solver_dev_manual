.. _iriclib_output_result:

計算結果の出力
==============

CGNSファイルに、計算結果を出力します。

特定の時間での計算結果を出力する前に、必ず :ref:`iriclib_output_time` で示した
時刻(もしくはループ回数) の出力を行ってください。

iRIClib で出力できる計算結果は、大きく以下に分類されます。

* 格子点に関係なく、1つのタイムステップで1つ値を持つ計算結果
* 格子点ごとに値を持つ計算結果

.. list-table:: 1つのタイムステップで1つ値を持つ計算結果の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_write_sol_baseiterative_integer_f
     - 整数の計算結果を出力する
   * - cg_iric_write_sol_baseiterative_real_f
     - 倍精度実数の計算結果を出力する

.. list-table:: 格子点ごとに値を持つ計算結果の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_write_sol_integer_f
     - 整数の格子点ごとに値を持つ計算結果を出力する
   * - cg_iric_write_sol_real_f
     - 倍精度実数の格子点ごとに値を持つ計算結果を出力する

.. list-table:: 粒子ごとに値を持つ計算結果の出力に利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_write_sol_particle_pos2d_f
     - 粒子の位置を出力する (2次元)
   * - cg_iric_write_sol_particle_pos3d_f
     - 粒子の位置を出力する (3次元)
   * - cg_iric_write_sol_particle_integer_f
     - 整数の粒子ごとに値を持つ計算結果を出力する
   * - cg_iric_write_sol_particle_real_f
     - 倍精度実数の粒子ごとに値を持つ計算結果を出力する

.. list-table:: 計算結果の出力の開始前、終了後に利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - iric_check_cancel_f
     - ユーザがソルバーの実行をキャンセルしたか確認する
   * - iric_check_lock_f
     - CGNSファイルが GUI によってロックされているか確認する
   * - iric_write_sol_start_f
     - 計算結果の出力開始をGUIに通知する
   * - iric_write_sol_end_f
     - 計算結果の出力終了をGUIに通知する
   * - cg_iric_flush_f
     - 計算結果の出力をファイルに書き込む

計算結果を出力する処理の例を :numref:`example_output_calc_result` に示します。

.. code-block:: fortran
   :caption: 計算結果を出力する処理の記述例
   :name: example_output_calc_result
   :linenos:

   program Sample6
     implicit none
     include 'cgnslib_f.h'

     integer:: fin, ier, isize, jsize
     integer:: canceled
     integer:: locked
     double precision:: time
     double precision:: convergence
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     real, dimension(:,:), allocatable:: velocity_x, velocity_y, depth
     integer, dimension(:,:), allocatable:: wetflag
     double precision, dimension(:,:), allocatable:: velocity_x, velocity_y, depth

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
     ! 計算結果を保持するメモリも確保
     allocate(velocity_x(isize,jsize), velocity_y(isize,jsize), depth(isize, jsize), wetflag(isize,jsize))
     allocate(particlex(10), particley(10))
     ! 格子を読み込む
     call cg_iric_getgridcoord2d_f (grid_x, grid_y, ier)

     ! 初期状態の情報を出力
     time = 0
     convergence = 0.1
     call cg_iric_write_sol_time_f(time, ier)
     ! 格子を出力
     call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
     ! 計算結果を出力
     call cg_iric_write_sol_real_f ('VelocityX', velocity_x, ier)
     call cg_iric_write_sol_real_f ('VelocityY', velocity_y, ier)
     call cg_iric_write_sol_real_f ('Depth', depth, ier)
     call cg_iric_write_sol_integer_f ('Wet', wetflag, ier)
     call cg_iric_write_sol_baseiterative_real_f ('Convergence', convergence, ier)
     do
       time = time + 10.0
       ! (ここで計算を実行。格子の形状も変化)
       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit
       call iric_check_lock_f('test.cgn', locked)
       do while (locked == 1)
         sleep(1)
         call iric_check_lock_f(condFile, locked)
       end do
       call iric_write_sol_start_f(condFile, ier)
       call cg_iric_write_sol_time_f(time, ier)
       ! 格子を出力
       call cg_iric_write_sol_gridcoord2d_f (grid_x, grid_y, ier)
       ! 計算結果を出力
       call cg_iric_write_sol_real_f ('VelocityX', velocity_x, ier)
       call cg_iric_write_sol_real_f ('VelocityY', velocity_y, ier)
       call cg_iric_write_sol_real_f ('Depth', depth, ier)
       call cg_iric_write_sol_integer_f ('Wet', wetflag, ier)
       call cg_iric_write_sol_baseiterative_real_f ('Convergence', convergence, ier)
       call cg_iric_write_sol_particle_pos2d_f(10, particlex, particley, ier)
       call cg_iric_flush_f('test.cgn', fin, ier)
       call iric_write_sol_end_f('test.cgn', ier)

       if (time > 1000) exit
     end do

     ! CGNS ファイルのクローズ
     call cg_close_f(fin, ier)
     stop
   end program Sample6


なお、iRIClib では、ベクトル量の計算結果とスカラー量の計算結果では、
同じ関数を使って出力を行います。ベクトル量の計算結果を出力する場合は、
上記で示したように \"VelocityX\", \"VelocityY\" などの名前で各成分を出力してください。

計算結果については、iRIC では特別な名前が定義されており、
特定の目的で使用される結果ではその名前を使用する必要があります。
特別な計算結果の名前については :ref:`special_result_names` を参照してください。
