内部変数の初期化
===================

開いた CGNS ファイルを、 iRIClib から利用するための準備をします。
CGNS ファイルを開いた後、いずれかを必ず実行します。

書き込みを行う場合には CG_MODE_MODIFYモードでCGNSファイルを開き、
cg_iric_init_fにより初期化します。

読み込み専用の場合には、CG_MODE_READモードでCGNSファイルを開き、
cg_iric_initread_fにより初期化します。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_init_f
     - 指定したファイルを読み込み・書き込み用にiRIClibから利用するため、内部変数を初期化し、ファイルを初期化する
   * - cg_iric_initread_f
     - 指定したファイルを読み込み専用でiRIClibから利用するため、内部変数を初期化する
