格子生成条件の読み込み処理の記述
---------------------------------

格子生成条件の読み込み処理を記述します。

iRIC は、 :ref:`how_to_create_gridgen_def_file` で作成した
定義ファイルに従って格子生成条件を格子生成データファイルに出力しますので、
それに対応するように格子生成条件の読み込み処理を記述します。

格子生成条件の読み込み処理を追記したソースコードを
:numref:`gridgenerator_with_grid_loadgridgencond`
に示します。追記した部分を太字で示します。格子生成条件を読み込む関数に
渡す引数が、 :ref:`gridgendef_define_gridgencond`
で定義ファイルに記述したItem 要素の name 属性と一致していることに
注目してください。

コンパイルしたら、 :ref:`gridgenerator_add_groudoutput`
の時と同様の手順で格子を生成し、指定した通りの格子生成条件で
格子が生成することを確認してください。

定義ファイルで定義する格子生成条件と、それを読み込むための iRIClib
の関数の対応関係については、:ref:`calccond_def_examples`
を参照してください。格子生成条件の読み込みに使う関数の詳細については、
:ref:`iriclib_load_calccond` を参照してください。

.. code-block:: fortran
   :caption: 格子生成条件の読み込み処理を追記したソースコード
   :name: gridgenerator_with_grid_loadgridgencond
   :linenos:
   :emphasize-lines: 8-9,11,29-34,38,45,51-53

   program SampleProgram
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier
     integer:: icount, istatus
     integer:: imax, jmax
     integer:: elev_on
     double precision:: elev_value
     double precision, dimension(:,:), allocatable::grid_x, grid_y
     double precision, dimension(:,:), elevation
   
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
   
     ! 格子生成条件の読み込み
     ! 簡潔に記述するため、エラー処理は行っていない
     call cg_iric_read_integer_f("imax", imax, ier)
     call cg_iric_read_integer_f("jmax", jmax, ier)
     call cg_iric_read_integer_f("elev_on", elev_on, ier)
     call cg_iric_read_real_f("elev_value", elev_value, ier)
   
     ! 格子生成用のメモリを確保
     allocate(grid_x(imax,jmax), grid_y(imax,jmax)
     allocate(elevation(imax,jmax))
   
     ! 格子を生成
     do i = 1, isize
       do j = 1, jsize
         grid_x(i, j) = i
         grid_y(i, j) = j
         elevation(i, j) = elev_value
       end do
     end do
   
     ! 格子を出力
     cg_iric_writegridcoord2d_f(imax, jmax, grid_x, grid_y, ier)
     if (elev_on == 1) then
       cg_iric_write_grid_real_node_f("Elevation", elevation, ier);
     end if
   
     ! 格子生成データファイルを閉じる
     call cg_close_f(fin, ier)
   end program SampleProgram
