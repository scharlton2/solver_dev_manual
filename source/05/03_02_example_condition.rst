.. _example_of_conditions:

Example of condition to activate calculation conditions etc.
=============================================================

Examples of conditions to activate calculation conditions, grid
generating conditions, and boundary conditions are shown in this
subsection. As these examples show, complex conditions can be defined
using conditions with types \\"and\\" and \\"or\\".


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
