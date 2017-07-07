.. _gridgendef_define_gridgencond:

格子生成条件の定義
-------------------

計算条件を定義します。計算条件は、ソルバー定義ファイルの
CalculationCondition 要素で定義します。 :ref:`gridgendef_create_basic_info`
で作成した格子生成プログラム定義ファイルに追記し、 :numref:`gridgendef_example_with_gridgencond`
に示すようなファイルにし、保存します。追記した部分を強調して示しました。

.. code-block:: xml
   :caption: 格子生成条件を追記した格子生成プログラム定義ファイルの例
   :name: gridgendef_example_with_gridgencond
   :linenos:
   :emphasize-lines: 11-18

   <?xml version="1.0" encoding="UTF-8"?>
   <GridGeneratorDefinition 
     name="samplecreator"
     caption="Sample Grid Creator"
     version="1.0"
     copyright="Example Company"
     executable="generator.exe"
     gridtype="structured2d"
   >
     <GridGeneratingCondition>
       <Tab name="size" caption="Grid Size">
         <Item name="imax" caption="IMax">
           <Definition valueType="integer" default="10" max="10000" min="1" />
         </Item>
         <Item name="jmax" caption="JMax">
           <Definition valueType="integer" default="10" max="10000" min="1" />
         </Item>
       </Tab>
     </GridGeneratingCondition>
   </GridGeneratorDefinition>

この時点では、格子生成プログラム定義ファイルの構造は
:numref:`gridgen_structure_with_gridgencond`
に示すようになっています。

.. _gridgen_structure_with_gridgencond:

.. figure:: images/gridgen_structure_with_gridgencond.png

   格子生成プログラム定義ファイルの構造

正しく格子生成プログラム定義ファイルが作成できているか確認します。

iRIC を起動し、 :ref:`gridgendef_create_basic_info` と同じ手順で
格子生成アルゴリズム選択画面を表示します。
"Sample Grid Creator" を選択し、 "OK" ボタンを押します。

すると、 :numref:`gridgen_cond_dialog_base` に示すダイアログが
表示されます。
:numref:`gridgendef_example_with_gridgencond` で追記した内容に従って、
"Grid Size" というグループが追加されているのが分かります。
確認できたら、 "キャンセル" ボタンを押します。

.. _gridgen_cond_dialog_base:

.. figure:: images/gridgen_cond_dialog_base.png

   格子生成ダイアログ 表示例

グループを増やして、さらに格子生成条件を追加します。
"Grid Size" の Tab要素 のすぐ下に、 "Elevation Output" というグループを
追加して保存します。追記した定義ファイルの抜粋を、
:numref:`gridgendef_example_with_gridgencond_advanced` に示します。
追記した部分を強調して示しました。

.. code-block:: xml
   :caption: 格子生成条件を追記した格子生成プログラム定義ファイルの例 (抜粋)
   :name: gridgendef_example_with_gridgencond_advanced
   :linenos:
   :emphasize-lines: 3-15

       (前略)
       </Tab>
       <Tab name="elevation" caption="Elevation Output">
         <Item name="elev_on" caption="Output">
           <Definition valueType="integer" default="0">
             <Enumeration caption="Enabled" value="1" />
             <Enumeration caption="Disabled" value="0" />
           </Definition>
         </Item>
         <Item name="elev_value" caption="Value">
           <Definition valueType="real" default="0">
             <Condition type="isEqual" target="elev_on" value="1" />
           </Definition>
         </Item>
       </Tab>
     </GridGeneratingCondition>
   </GridGeneratorDefinition>


この時点では、定義ファイルの構造は
:numref:`gridgen_structure_with_gridgencond_advanced` に示す通りです。

.. _gridgen_structure_with_gridgencond_advanced:

.. figure:: images/gridgen_structure_with_gridgencond_advanced.png

   格子生成プログラム定義ファイルの構造


正しくソルバー定義ファイルが作成できているか確認します。
先ほどと同じ手順でダイアログを表示します。

"Elevation Output" というグループがリストに表示され、
このグループには2つの項目が表示されているのが分かります。
また、 "Value" は、 "Output" で "Enabled" を選択している時のみ有効です。
ダイアログの表示例を :numref:`gridgen_cond_dialog_advanced` に示します。

.. _gridgen_cond_dialog_advanced:

.. figure:: images/gridgen_cond_dialog_advanced.png

   格子生成ダイアログ 表示例

格子生成条件の定義についてまとめると、以下の通りです。

- 格子生成条件のグループは Tab 要素で、格子生成条件は Item 要素でそれぞれ指定します。

- Definition 要素以下の構造は、計算条件の種類 (例: 整数、実数、整数からの選択、関数型)
  によって異なります。格子生成条件の種類ごとの記述方法と、ダイアログ上での表示については
  5.3.1 を参照して下さい。

- 格子生成条件には、 Condition 要素で依存関係を定義できます。 Condition 要素では、
  その格子生成条件が有効になる条件を指定します。 Condition 要素の定義方法の詳細は、
  5.3.2 を参照して下さい。

- この例では、格子生成条件のダイアログを単純なリスト形式で作成しましたが、
  グループボックスを使うなどしてダイアログのレイアウトをカスタマイズすることができます。
  ダイアログのレイアウトのカスタマイズ方法については 5.3.3 を参照して下さい。
