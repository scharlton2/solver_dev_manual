単純なレイアウト
-------------------

Item 要素 のみを使って定義した単純なレイアウトの例を
:numref:`layout_example_basic_code` に、
ダイアログでの表示例を :numref:`layout_example_basic_image` に
それぞれ示します。

.. code-block:: xml
   :name: layout_example_basic_code
   :linenos:

   <Tab name="simple" caption="Simple">
     <Item name="jrep" caption="Periodic boundary condition">
       <Definition valueType="integer" default="0">
         <Enumeration value="0" caption="Disabled"/>
         <Enumeration value="1" caption="Enabled"/>
       </Definition>
     </Item>
     <Item name="j_wl" caption="Water surface at downstream">
       <Definition valueType="integer" default="1">
         <Enumeration value="0" caption="Constant value"/>
         <Enumeration value="1" caption="Uniform flow"/>
         <Enumeration value="2" caption="Read from file"/>
       </Definition>
     </Item>
     <Item name="h_down" caption="   Constant value (m)">
       <Definition valueType="real" default="0" />
     </Item>
     <Item name="j_slope" caption="   Slope for uniform flow">
       <Definition valueType="integer" default="0">
         <Enumeration value="0" caption="Calculated from geographic data"/>
         <Enumeration value="1" caption="Constant value"/>
       </Definition>
     </Item>
     <Item name="bh_slope" caption="   Slope value at downstream">
       <Definition valueType="real" default="0.001">
       </Definition>
     </Item>
     <Item name="j_upv" caption="Velocity at upstream">
       <Definition valueType="integer" default="1">
         <Enumeration value="1" caption="Uniform flow"/>
         <Enumeration value="2" caption="Calculated from upstream depth"/>
       </Definition>
     </Item>
     <Item name="j_upv_slope" caption="   Slope for uniform flow">
       <Definition valueType="integer" default="0">
         <Enumeration value="0" caption="Calculated from geographic data"/>
         <Enumeration value="1" caption="Constant value"/>
       </Definition>
     </Item>
     <Item name="upv_slope" caption="   Slope value at upstream">
       <Definition valueType="real" default="0.001">
       </Definition>
     </Item>
   </Tab>

.. _layout_example_basic_image:

.. figure:: images/layout_simple.png

   単純なレイアウトのダイアログの表示例
