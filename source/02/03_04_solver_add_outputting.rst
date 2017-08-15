.. _solver_dev_add_outputting:


時刻、計算結果の出力処理の記述
------------------------------

時刻、計算結果の出力処理を記述します。

時間依存の方程式を解くソルバーの場合、タイムステップの数だけ時刻、
計算結果の出力を繰り返します。

また、時刻、計算結果の出力のたびにユーザがソルバーの実行を中止していないか確認し、
中止していたら実行を中止します。

なお、ソルバーが出力する計算結果についてはソルバー定義ファイルには記述しませんので、
ソルバー定義ファイルとの対応関係を気にせず記述できます。

時刻、計算結果の出力処理を追記したソースコードを
:numref:`solver_with_outputting` に示します。強調して示したのが追記した部分です。

.. code-block:: fortran
   :caption: 時刻、計算結果の出力処理を追記したソースコード
   :name: solver_with_outputting
   :linenos:
   :emphasize-lines: 6-13,21-49

     ! (略)
     integer:: isize, jsize
     double precision, dimension(:,:), allocatable:: grid_x, grid_y
     double precision, dimension(:,:), allocatable:: elevation
     integer, dimension(:,:), allocatable:: obstacle
     double precision:: time
     integer:: iteration
     integer:: canceled
     integer:: locked
     double precision, dimension(:,:), allocatable:: velocity_x, velocity_y
     double precision, dimension(:,:), allocatable:: depth
     integer, dimension(:,:), allocatable:: wetflag
     double precision:: convergence

     ! (略)

     ! 属性を読み込む
     call cg_iric_read_grid_real_node_f("Elevation", elevation, ier)
     call cg_iric_read_grid_integer_cell_f("Obstacle", obstacle, ier)

     allocate(velocity_x(isize,jsize), velocity_y(isize,jsize), depth(isize,jsize), wetflag(isize,jsize))
     iteration = 0
     time = 0
     do
       time = time + timestep
       ! (ここで計算を実行。格子の形状も変化)

       call iric_check_cancel_f(canceled)
       if (canceled == 1) exit
       call iric_check_lock_f(condFile, locked)
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
       call cg_iric_flush_f(condFile, fin, ier)
       call iric_write_sol_end_f(condFile, ier)
       iteration = iteration + 1
       if (iteration > maxiterations) exit
     end do
   
     ! 計算データファイルを閉じる
     call cg_close_f(fin, ier)
     stop
   end program SampleProgram



時刻、計算結果の出力に使う関数の詳細については、
:ref:`iriclib_output_time`, :ref:`iriclib_output_result` を参照してください。
計算実行中に格子形状が変化する場合、
:ref:`iriclib_output_grid_in_sol` で説明する関数を使用してください。

計算結果については、iRIC では特別な名前が定義されており、
特定の目的で使用される結果ではその名前を使用する必要があります。
特別な計算結果の名前については :ref:`special_result_names` を参照してください。
