.. _iriclib_load_calccond:

計算条件 (もしくは格子生成条件) の読み込み
==============================================

CGNSファイルから、計算条件 (もしくは格子生成条件) を読み込みます。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_read_integer_f
     - 整数の条件を読み込む
   * - cg_iric_read_real_f
     - 倍精度実数の条件を読み込む
   * - cg_iric_read_realsingle_f
     - 単精度実数の条件を読み込む
   * - cg_iric_read_string_f
     - 文字列の条件を読み込む
   * - cg_iric_read_functionalsize_f
     - 関数型の条件のサイズを調べる
   * - cg_iric_read_functional_f
     - 倍精度実数の関数型の条件を読み込む
   * - cg_iric_read_functional_realsingle_f
     - 単精度実数の関数型の条件を読み込む
   * - cg_iric_read_functionalwithname_f
     - 値を複数持つ倍精度実数の関数型の条件を読み込む

関数型以外の条件については、一つの関数で一つの条件を読み込むことができます。
整数の計算条件を読み込む処理の例を :numref:`example_load_integer_calccond` に示します。

.. code-block:: fortran
   :caption: 整数型の計算条件を読み込む処理の記述例
   :name: example_load_integer_calccond
   :linenos:

   program Sample1
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, i_flow
   
     ! CGNS ファイルのオープン
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! 内部変数の初期化
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     call cg_iric_read_integer_f('i_flow', i_flow, ier)
     print *, i_flow;
   
     ! CGNS ファイルのクローズ
     call cg_close_f(fin, ier)
     stop
   end program Sample1

 
一方、関数型の計算条件では、cg_iric_read_functionalsize_f, cg_iric_read_functional_f の
二つの関数を利用する必要があります。関数型の計算条件を読み込む処理の例を
:numref:`example_load_functional_calccond` に示します。

.. code-block:: fortran
   :caption: 関数型の計算条件を読み込む処理の記述例
   :name: example_load_functional_calccond
   :linenos:

   program Sample2
     implicit none
     include 'cgnslib_f.h'
   
     integer:: fin, ier, discharge_size, i
     double precision, dimension(:), allocatable:: discharge_time, discharge_value  ! discharge の時刻と値を保持する配列
   
     ! CGNS ファイルのオープン
     call cg_open_f('test.cgn', CG_MODE_MODIFY, fin, ier)
     if (ier /=0) STOP "*** Open error of CGNS file ***"
   
     ! 内部変数の初期化
     call cg_iric_init_f(fin, ier)
     if (ier /=0) STOP "*** Initialize error of CGNS file ***"
   
     ! まず、関数型の入力条件のサイズを調べる
     call cg_iric_read_functionalsize_f('discharge', discharge_size, ier)
     ! メモリを確保
     allocate(discharge_time(discharge_size), discharge_value(discharge_size))
     ! 確保したメモリに値を読み込む
     call cg_iric_read_functional_f('discharge', discharge_time, discharge_value, ier)
   
     ! （出力）
     if (ier ==0) then
       print *, 'discharge: discharge_size=', discharge_size
       do i = 1, min(discharge_size, 5)
         print *, ' i,time,value:', i, discharge_time(i), discharge_value(i)
       end do
     end if
   
     ! allocate で確保したメモリを開放
     deallocate(discharge_time, discharge_value)
   
     ! CGNS ファイルのクローズ
     call cg_close_f(fin, ier)
     stop
   end program Sample2

計算条件 (もしくは 格子生成条件) の種類別の読み込み処理の記述例については、
:ref:`calccond_def_examples` を参照してください。
