SolverDefinition
================

ソルバーの定義情報を保持します。

例
----

.. code-block:: xml
   :caption: SolverDefinition の定義例
   :name: ref_solverdefinition_example
   :linenos:


   <SolverDefinition
     name="samplesolver"
     caption="Sample Solver 1.0"
     version="1.0"
     copyright="Example Company"
     release="2012.04.01"
     homepage="http://example.com/"
     executable="solver.exe"
     iterationtype="time"
     gridtype="structured2d"
   >
     <CalculationCondition>

       (略)

     </CalculationCondition>
     <GridRelatedCondition>

       (略)

     </GridRelatedCondition>
   </SolverDefinition>

属性
-----

.. csv-table:: SolverDefinition の属性
   :file: solverdefinition_attributes.csv
   :header-rows: 1

.. csv-table:: iterationtype の値
   :file: solverdefinition_att_iterationtype.csv
   :header-rows: 1

.. csv-table:: gridtype の値
   :file: solverdefinition_att_gridtype.csv
   :header-rows: 1

ソルバーのバージョンアップを行う時は、 version 属性を変更します。
ソルバーのバージョンアップ時の注意点については、
:ref:`notice_about_version` を参照して下さい。

子要素
--------

.. csv-table:: SolverDefinition の子要素
   :file: solverdefinition_elements.csv
   :header-rows: 1
