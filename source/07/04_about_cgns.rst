.. _about_cgns:

CGNS ファイル、 CGNSライブラリに関する情報
===========================================

CGNS ファイルフォーマットの概要
-------------------------------

CGNSは、CFG General Notation System の略で、数値流体力学で用いられるデータを
格納するための汎用ファイルフォーマットです。
OS やCPU の種類が異なるコンピュータの間で、共通して利用することができます。
数値流体力学で用いられる標準的なデータ形式が定義されているほか、
ソルバーごとに独自の要素を追加する拡張性が備わっています。

CGNS ファイルの入出力ライブラリは cgnslib として提供されており、
以下の言語から利用することができます。

* C, C++
* FORTRAN
* Python

元は Boeing 社と NASA が共同で開発しましたが、現在はオープンソースの
コミュニティによって機能追加やメンテナンスが行われています。

CGNS ファイルの閲覧方法
-----------------------

ここでは、iRIC により作成した CGNS ファイルを HDFView を用いて
閲覧する方法を説明します。HDFView は、フリーソフトとして
公開されているソフトウェアです。

HDFView のインストール
~~~~~~~~~~~~~~~~~~~~~~~

まず、HDFViewをインストールします。HDFView のインストーラは、
以下のサイトからダウンロードできます。

https://www.hdfgroup.org/downloads/index.html

.. _hdfview_webpage:

.. figure:: images/hdf_webpage.png

   HDF group ウェブページ

HDF のホームページから、「Current Release」の
リンクをクリックします。すると、様々なファイルのダウンロード画面に
移動します。ここで、適切な (64 bit or 32 bit)
プラットフォームのインストーラをクリックしてダウンロードしてください。
解凍してインストーラを実行することで、 HDFViewがインストールされます。

.. _hdfview_download_page:

.. figure:: images/hdf_downloadpage.png

   ダウンロードページ 表示例

HDFView を利用したCGNS ファイルの閲覧
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HDFViewを起動して CGNS ファイルを閲覧します。

まず、スタートメニューから HDFView を起動します。次に、以下のメニューから、
開く CGNS ファイルを選択します。

File --> Open

HDFView では、拡張子 \\"\*.cgn\\" のファイルはデフォルトでは開く対象に含まれないため、
ファイルのタイプで「すべてのファイル」を指定した上で、CGNSファイルを選択して開いて下さい。
CGNS ファイルを開いた後の HDFView の画面表示例を
:numref:`hdfview_example` に示します。
 
.. _hdfview_example:

.. figure:: images/hdfview.png

   HDFView 表示例

画面の左側には、CGNS ファイル内のツリー構造が表示されます。
ツリー構造で、閲覧したい項目を選択すると、画面右側に選択した項目の
内部のデータが表示されます。
 
リンク集
---------

CGNS ファイル及び CGNS ライブラリに関する情報は、 :numref:`cgns_links`
を参照してください。

.. _cgns_links:

.. list-table:: CGNS ファイル、CGNSライブラリ関連リンク
   :header-rows: 1

   * - 項目
     - URL
   * - ホームページ
     - http://cgns.sourceforge.net/
   * - 関数リファレンス
     - http://www.grc.nasa.gov/WWW/cgns/midlevel/index.html
   * - CGNSファイルの内部構造
     - http://www.grc.nasa.gov/WWW/cgns/sids/index.html
   * - CGNSライブラリの利用プログラムの記述例集
     - http://sourceforge.net/projects/cgns/files/UserGuideCode/Release%203/UserGuideCodeV3.zip/download
