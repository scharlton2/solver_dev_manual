.. _gridgendef_create_basic_info:

Defining basic information
---------------------------

Define basic information of a grid generating program. Create a file
with the content shown in :numref:`gridgendef_example1`, and save it
with name \"definition.xml\" under \"example\" folder that you created in
:ref:`create_gridgen_folder`.

.. code-block:: xml
   :caption: Example grid generating program definition file that contains basic information
   :name: gridgendef_example1
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
   <GridGeneratorDefinition
     name="samplecreator"
     caption="Sample Grid Creator"
     version="1.0"
     copyright="Example Company"
     executable="generator.exe"
     gridtype="structured2d"
   >
     <GridGeneratingCondition>
     </GridGeneratingCondition>
   </GridGeneratorDefinition>

At this point, the structure of the grid generating program definition
file is as shown in :numref:`gridgendef_structure1`.

.. _gridgendef_structure1:

.. figure:: images/gridgendef_structure1.png
   :width: 400pt

   Grid generating program definition file structure

Now make sure the grid generating file definition file is arranged
correctly.

Launch iRIC. The [iRIC Start Page] dialog (:numref:`iric_start_dialog_for_gridgendef`)
is shown, so click on [New Project]. Now the [Solver Select] dialog
(:numref:`solver_select_dialog_for_gridgendef`) will
open, so select \"Nays2DH\" in the solver list, and click on [OK]. The new
project will start.

Open the [Select Grid Creating Algorithm] dialog
(:numref:`gridgen_select_dialog`) by processing the following action.

**Menu bar:** [Grid] (G) -> [Select Algorithm to Create Grid] (S)

Check that the \"Sample Grid Creator\" is added in the list. When you
finish checking, close the dialog by clicking on [Cancel].

.. _iric_start_dialog_for_gridgendef:

.. figure:: images/iric_start_dialog.png
   :width: 340pt

   The [iRIC Start Page] dialog

.. _solver_select_dialog_for_gridgendef:

.. figure:: images/solver_select_dialog.png
   :width: 360pt

   The [Select Solver] dialog

.. _gridgen_select_dialog:

.. figure:: images/gridgen_select_dialog.png
   :width: 360pt

   The [Select Grid Creating Algorithm] dialog
