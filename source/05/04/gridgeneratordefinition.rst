GridGeneratorDefinition
========================

GridGeneratorDefinition element contains definition information of the
grid generating program.

Example
---------

.. code-block:: xml
   :caption: Example of GridGeneratorDefinition
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

         (Abbr.)

       </Tab>
     </GridGeneratingCondition>
   </GridGeneratorDefinition>

Attributes
-----------

.. csv-table:: Attributes of GridGeneratorDefinition
   :file: gridgeneratordefinition_attributes.csv
   :header-rows: 1

.. csv-table:: gridType values
   :file: gridgeneratordefinition_att_gridtype.csv
   :header-rows: 1


Child elements
---------------

.. csv-table:: Child elements of GridGeneratingCondition
   :file: gridgeneratordefinition_elements.csv
   :header-rows: 1
