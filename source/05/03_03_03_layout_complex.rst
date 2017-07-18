.. _free_layout_example:
Free layout
------------

Free layout example, that uses GridLayout element, is shown in
:numref:`layout_example_complex_code`, 
and the corresponsing dialog is shown in
:numref:`layout_example_complex_image`.

GridLayout, HBoxLayout, VBoxLayout can be used to layout widgets freely.
When using these elements for layouting, caption attributes are not used
to show labels, but Label elements are used to show labels instead.

GridLayout, HBoxLayout, VBoxLayout elements can be used recursively.
GroupBox element can be used inside these elements freely.

.. code-block:: xml
   :caption: Free layout definition example
   :name: layout_example_complex_code
   :linenos:

   <Tab name="roughness" caption="Roughness">
     <Item name="diam" caption="Diameter of uniform bed material (mm)">
       <Definition valueType="real" default="0.55" />
     </Item>
     <Item name="j_drg" caption="Bed roughness">
       <Definition valueType="integer" default="0">
         <Enumeration value="0" caption="Calculated from bed material"/>
         <Enumeration value="1" caption="Constant value"/>
         <Enumeration value="2" caption="Read from file"/>
       </Definition>
     </Item>
     <GroupBox caption="Manning's roughness parameter">
       <GridLayout>
         <Label row="0" col="0" caption="Low water channel" />
         <Item row="1" col="0" name="sn_l">
           <Definition valueType="real" default="0.01" />
         </Item>
         <Label row="0" col="1" caption="Flood channel" />
         <Item row="1" col="1" name="sn_h">
           <Definition valueType="real" default="0.01" />
         </Item>
         <Label row="0" col="2" caption="Fixed bed" />
         <Item row="1" col="2" name="sn_f">
           <Definition valueType="real" default="0.01" />
         </Item>
       </GridLayout>
     </GroupBox>
     <Item name="snfile" caption="Input file for Manning's roughness">
       <Definition valueType="filename" default="Select File" />
     </Item>
   </Tab>

.. _layout_example_complex_image:

.. figure:: images/layout_complex.png

   Dialog for free layout definition example
