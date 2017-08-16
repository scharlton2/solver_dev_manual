GroupBox
=========

GroupBox element contains information that defines a group box to be
displayed in the calculation condition input dialog or grid generating
condition input dialog.

Example
--------

.. code-block:: xml
   :caption: Example of GroupBox definition
   :name: ref_groupbox_example
   :linenos:

   <GroupBox caption="Time">
     <Item name="stime" caption="Start Time">
       <Definition valueType="real" />
     </Item>
     <Item name="etime" caption="End Time">
       <Definition valueType="real" />
     </Item>
   </GroupBox>

Refer to :ref:`layout_groupbox_example` for an example of
GroupBox element definition.

Attributes
----------

.. csv-table:: Attributes of GroupBox
   :file: groupbox_attributes.csv
   :header-rows: 1

Child elements
--------------

.. csv-table:: Child elements of GroupBox
   :file: groupbox_elements.csv
   :header-rows: 1
