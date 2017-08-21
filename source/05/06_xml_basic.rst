.. _xml_basics:

XML の基礎
===========

この節では、iRIC でソルバー定義ファイル、格子生成プログラム定義ファイルに
用いられているXMLという言語の基礎について説明します。

要素の書き方
-------------

要素の開始は、要素名を \"<\" と \">\" で囲って記述します。

要素の終了は、要素名を \"</\" と \">\" で囲って記述します。

Item 要素の記述例を :numref:`xml_element_example` に示します。

.. code-block:: xml
   :caption: 要素の記述例
   :name: xml_element_example

   <Item>
   
   </Item>

要素は、以下を持つことができます。

- 子要素
- 属性

要素は、同じ名前の子要素を複数持つことができます。
一方、属性は同じ名前の属性は1つしか持てません。
子要素 SubItem と、属性 name を持つ Item 要素の記述例を
:numref:`xml_element_example2` に示します。

.. code-block:: xml
   :caption: 要素の記述例
   :name: xml_element_example2

   <Item name="sample">
     <SubItem>
     </SubItem>
     
     <SubItem>
     </SubItem>
   </Item>

また、子要素を持たない要素は \"<要素名 />\"
という形式で記述できます。例えば、
:numref:`xml_element_without_child_example`,
:numref:`xml_element_without_child_example2`
の要素は、読み込まれると同じデータとして処理されます。

.. code-block:: xml
   :caption: 子要素を持たない要素の記述例
   :name: xml_element_without_child_example

   <Item name="sample">
   
   </Item>

.. code-block:: xml
   :caption: 子要素を持たない要素の記述例
   :name: xml_element_without_child_example2

   <Item name="sample" />

タブ、スペース、改行について
-----------------------------

XML では、タブ、スペース、改行は無視されますので、XML
を読みやすくするために自由に追加できます。ただし、
属性の値の中のスペースなどは無視されません。

:numref:`xml_element_spaces_example`,
:numref:`xml_element_spaces_example2`,
:numref:`xml_element_spaces_example3` の要素は、
読み込まれるとすべて同じデータとして処理されます。

.. code-block:: xml
   :caption: 要素の記述例
   :name: xml_element_spaces_example

   <Item name="sample">
     <SubItem>
     </SubItem>
   </Item>

.. code-block:: xml
   :caption: 要素の記述例
   :name: xml_element_spaces_example2

   <Item
     name="sample"
   >
     <SubItem></SubItem>
   </Item>

.. code-block:: xml
   :caption: 要素の記述例
   :name: xml_element_spaces_example3

   <Item name="sample"><SubItem></SubItem></Item>

コメントの書き方
----------------

XML では、\"<!--\" と \"-->\" で囲まれた間がコメントになります。
:numref:`xml_element_comment_example`
にコメントの記述例を示します。

.. code-block:: xml
   :caption: コメントの記述例
   :name: xml_element_comment_example

   <!-- この部分はコメントになります。-->
   <Item name="sample">
     <SubItem>
     </SubItem>
   </Item>
