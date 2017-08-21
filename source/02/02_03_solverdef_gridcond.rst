.. _solverdef_define_gridcond:

格子属性の定義
--------------

格子属性を定義します。格子属性は、ソルバー定義ファイルの
GridRelatedCondition 要素で定義します。 :ref:`solverdef_define_calccond`
で作成したソルバー定義ファイルに追記し、 GridRelatedCondition 要素に
:numref:`solverdef_example_with_gridcond` 
に示すように追記し、保存します。追記した部分を強調して示しました。

.. code-block:: xml
   :caption: 格子属性を追記したソルバー定義ファイルの例 (抜粋)
   :name: solverdef_example_with_gridcond
   :linenos:
   :emphasize-lines: 4-17

   (前略)
     </CalculationCondition>
     <GridRelatedCondition>
       <Item name="Elevation" caption="Elevation">
         <Definition position="node" valueType="real" default="max" />
       </Item>
       <Item name="Obstacle" caption="Obstacle">
         <Definition position="cell" valueType="integer" default="0">
           <Enumeration value="0" caption="Normal cell" />
           <Enumeration value="1" caption="Obstacle" />
         </Definition>
       </Item>
       <Item name="Rain" caption="Rain">
         <Definition position="cell" valueType="real" default="0">
           <Dimension name="Time" caption="Time" valueType="real" />
         </Definition>
       </Item>
     </GridRelatedCondition>
   </SolverDefinition>


正しくソルバー定義ファイルが作成できているか確認します。


iRIC を起動して、ソルバー \"Sample Solver\" の新しいプロジェクトを開始します。
すると、 :numref:`preprocessor_with_geographicdata` に示すような画面が
表示されます。さらに、格子を作成したりインポートしたりすると、
:numref:`preprocessor_with_gridattributes` のようになります。

なお、格子の作成やインポートの方法が分からない場合、ユーザマニュアルを参照して下さい。

.. _preprocessor_with_geographicdata:

.. figure:: images/preprocessor_with_geographicdata.png

   プリプロセッサ 表示例

.. _preprocessor_with_gridattributes:

.. figure:: images/preprocessor_with_gridattributes.png

   プリプロセッサ 表示例 (格子生成後)

以下の手順で格子点の属性Elevation を編集すると、 :numref:`dialog_to_edit_elevation` に
示すダイアログが表示され、実数の値を入力できることが確認できます。

- オブジェクトブラウザで、 \"格子\" --> \"格子点の属性\" -> \"Elevation\" を選択します。
- 描画領域で、マウスクリックで格子点を選択します。
- 右クリックメニューを表示し、 \"編集\" を選択します。

.. _dialog_to_edit_elevation:

.. figure:: images/dialog_to_edit_elevation.png

   格子点の属性 \"Elevation\" の編集ダイアログ

同様に、格子セルの属性 \"Obstacle\" を編集すると、 :numref:`dialog_to_edit_obstacle` に示す
ダイアログが表示され、 :numref:`solverdef_example_with_gridcond` で
指定した選択肢から値を選択できることが確認できます。

.. _dialog_to_edit_obstacle:

.. figure:: images/dialog_to_edit_obstacle.png

   格子セルの属性 \"Obstacle\" の編集ダイアログ


格子属性の定義についてまとめると、以下の通りです。

- 格子属性は、Item要素で指定します。

- Item 要素以下の構造は計算条件の Item と基本的には同じですが、
  以下の違いがあります。

  - 属性を格子点で定義するか、セルで定義するかを position 属性で指定します。
  - 文字列、関数型、ファイル名、フォルダ名を指定することはできません。
  - 依存関係を指定することはできません。
  - Dimension要素を用いて、次元を定義することができます。

格子属性については、iRIC では特別な名前が定義されており、特定の目的で使用される
属性ではその名前を使用する必要があります。特別な格子属性の名前については
:ref:`special_names` を参照してください。
