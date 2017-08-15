.. _example_of_conditions:

計算条件・境界条件・格子生成条件の有効になる条件の定義例
========================================================

計算条件、格子生成条件、境界条件に関する有効になる条件の定義例を示します。
ここで示すように、type が "and", "or" の条件を利用
することによって複雑な条件を指定することができます。

var1 = 1
---------

.. code-block:: xml
   :name: cond_example1
   :linenos:

   <Condition type="isEqual" target="var1" value="1" />

var1 = 1 and var2 > 3
-----------------------

.. code-block:: xml
   :name: cond_example2
   :linenos:

   <Condition type="or">
     <Condition type="isEqual" target="var1" value="1" />
     <Condition type="isGreaterThan" target="var2" value="3" />
   </Condition>

(var1 = 1 or var2 < 5) and var3 = 100
---------------------------------------

.. code-block:: xml
   :name: cond_example3
   :linenos:

   <Condition type="and">
     <Condition type="or">
       <Condition type="isEqual" target="var1" value="1" />
       <Condition type="isLessThan" target="var2" value="5" />
     </Condition>
     <Condition type="isEqual" target="var3" value="100" />
   </Condition>
