.. _gridgendef_define_errorcode:

エラーコードの定義
------------------

格子生成プログラムで発生するエラーのコードと、対応するメッセージを定義します。
エラーコードは、定義ファイルの ErrorCode 要素で定義します。
:ref:`gridgendef_define_gridgencond` で作成した格子生成プログラム定義ファイル
に追記し、 :numref:`gridgendef_example_with_errorcode` に示すような
ファイルにし、保存します。追記した部分を強調して示しました。

.. code-block:: xml
   :caption: エラーコードを追記した格子生成プログラム定義ファイルの例
   :name: gridgendef_example_with_errorcode
   :linenos:
   :emphasize-lines: 5-7

   (前略)
         </Item>
       </Tab>
     </GridGeneratingCondition>
     <ErrorCodes>
       <ErrorCode value="1" caption="IMax * JMax must be smaller than 100,000." />
     </ErrorCodes>
   </GridGeneratorDefinition>

この時点では、定義ファイルの構造は :numref:`gridgendef_structure_with_error`
に示すようになっています。
なお、エラーコードの定義は必須ではありません。

.. _gridgendef_structure_with_error:

.. figure:: images/gridgendef_structure_with_error.png
   :width: 400pt

   格子生成プログラム定義ファイルの構造

エラーコードの定義が正しく行えているかの確認は、
格子生成プログラムを作成するまで行えません。
エラーコードの定義の確認については
:ref:`gridgenerator_add_errorhandling` で行います。
