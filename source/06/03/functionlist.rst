.. _iriclib_list_of_functions:

サブルーチン一覧
=================

サブルーチンとその分類の一覧を :numref:`iriclib_subroutine_list`
に示します。

.. _iriclib_subroutine_list:

.. csv-table:: iRIClibサブルーチン一覧
   :file: funclist.csv
   :header-rows: 1

なお、「複数版」欄が「○」となっているサブルーチン (単一CGNSファイル用) には、
ファイルIDを第一引数とする、類似のサブルーチン (複数CGNSファイル用) があります。
名前は、末尾の \"_f\" を \"_mul_f\" に変えたものです。

例えば、CGNSファイルから整数型の計算条件・格子生成条件の値を読み込む関数
には、以下のものがあります。


* 単一CGNSファイルを扱うプログラム用

.. code-block:: fortran

   call cg_iric_read_integer_f(label, intvalue, ier)

* 複数CGNSファイルを扱うプログラム用

.. code-block:: fortran

   call cg_iric_read_integer_mul_f(fid, label, intvalue, ier)

単一CGNSファイル用、複数CGNSファイル用の違いを :numref:`difference_single_mul` に示します。

.. _difference_single_mul:

.. list-table:: 単一・複数CGNSファイル用サブルーチンの違い
   :header-rows: 1

   * - 項目
     - 単一CGNSファイル用
     - 複数CGNSファイル用
   * - 名前
     - 末尾が \"_f\" (\"_mul\" が付かない)
     - 末尾が \"_mul_f\"
   * - 引数
     - 次節以降参照
     - 第一引数 = ファイルID (integer)
   * - 操作対象ファイル
     - 最後に cg_iric_init_f またはcg_iric_initread_f で指定したファイル
     - 第一引数で指定したファイル
