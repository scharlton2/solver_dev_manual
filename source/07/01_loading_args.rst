Fortran プログラムでの引数の読み込み処理
===========================================

iRICは、ソルバーや格子生成プログラムを起動する時、コマンドライン引数として
計算データファイルもしくは格子生成データファイルの名前を渡すため、
これを読み込む必要があります。

Fortran では、コマンドライン引数を読み込む方法がコンパイラによって異なります。
ここでは、Intel Fortran Compiler と、GNU Fortran (gfortran), G95 での
引数の読み込み処理について説明します。

Intel Fortran Compiler
------------------------

nargs()でコマンドライン引数の個数を取得し、引数がある場合、
getarg() で引数を取得します。

.. code-block:: fortran
   :caption: Intel Fortran Compiler での引数読み込み処理例
   :linenos:

   icount = nargs()  ! コマンド名が数に含まれるので、引数が1つなら2を返す
   if ( icount.eq.2 ) then
     call getarg(1, condFile, istatus)
   else
     write(*,*) “Input File not specified.”
     stop
   endif

GNU Fortran, G95
-----------------

iargc() でコマンドライン引数の個数を取得し、
引数がある場合、getarg() で引数を取得します。

Intel Fortran Compiler の nargs(), getarg() とは
仕様が異なりますので注意して下さい。

.. code-block:: fortran
   :caption: GNU Fortran, G95での引数読み込み処理例
   :linenos:

   icount = iargc()  ! コマンド名は数に含まれないので、引数が1つなら1を返す
   if ( icount.eq.1 ) then
     call getarg(0, str1)      ! 実行プログラムのファイル名
     call getarg(1, condfile)  ! 引数
   else
     write(*,*) "Input File not specified."
     stop
   endif

