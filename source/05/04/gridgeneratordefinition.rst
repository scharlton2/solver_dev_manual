GridGeneratorDefinition
========================

格子生成プログラムの定義情報を保持します。

例
----

.. code-block:: xml
   :caption: GridGeneratorDefinition の定義例
   :name: ref_gridgeneratordefinition_example
   :linenos:

   <GridGeneratorDefinition
     name="samplecreator"
     caption="Sample Grid Creator"
     version="1.0"
     copyright="Example Company"
     executable="generator.exe"
     gridtype="structured2d"
   >
     <GridGeneratingCondition>
       <Tab name="basic" caption="Basic Setting">

         (略)

       </Tab>
     </GridGeneratingCondition>
   </GridGeneratorDefinition>

属性
-----

.. csv-table:: GridGeneratorDefinition の属性
   :file: gridgeneratordefinition_attributes.csv
   :header-rows: 1

.. csv-table:: gridType の値
   :file: gridgeneratordefinition_att_gridtype.csv
   :header-rows: 1


子要素
--------

.. csv-table:: GridGeneratingCondition の子要素
   :file: gridgeneratordefinition_elements.csv
   :header-rows: 1
