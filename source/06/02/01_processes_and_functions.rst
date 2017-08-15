プログラムの処理とiRIClibの関数
=================================

ソルバー、格子生成プログラムで必要な入出力処理を :numref:`processses_of_solver_io` 、
:numref:`processses_of_gridgenerator_io` に示します。

.. list-table:: ソルバーの入出力処理
   :name: processses_of_solver_io
   :header-rows: 1

   * - 処理内容
   * - CGNS ファイルを開く
   * - 内部変数の初期化
   * - オプションの設定
   * - 計算条件の読み込み
   * - 計算格子の読み込み
   * - 境界条件の読み込み
   * - 地形データの読み込み (必要な場合のみ)
   * - 計算格子の出力 (格子の生成、再分割を行う場合のみ)
   * - 時刻 (もしくはループ回数) の出力
   * - 計算格子の出力 (移動格子の場合のみ)
   * - 計算結果の出力
   * - CGNSファイルを閉じる

.. list-table:: 格子生成プログラムの入出力処理
   :name: processses_of_gridgenerator_io
   :header-rows: 1

   * - 処理内容
   * - CGNS ファイルを開く
   * - 内部変数の初期化
   * - 格子生成条件の読み込み
   * - エラーコードの出力
   * - 格子の出力
   * - CGNSファイルを閉じる
