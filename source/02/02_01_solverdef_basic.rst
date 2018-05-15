.. _solverdef_create_basic_info:

Defining basic information
---------------------------

Define basic information of a solver. Create a file with the content
shown in :numref:`solverdef_example1`, and save it with name
\"definition.xml\" under \"example\" folder
that you created in :ref:`create_solverdef_folder`

.. code-block:: xml
   :caption: Example solver definition file that contains basic information
   :name: solverdef_example1
   :linenos:

   <?xml version="1.0" encoding="UTF-8"?>
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
     </CalculationCondition>
     <GridRelatedCondition>
     </GridRelatedCondition>
   </SolverDefinition>

At this point, the structure of the solver definition file is as shown
in :numref:`solverdef_structure1`.

.. _solverdef_structure1:

.. figure:: images/solverdef_structure1.png
   :width: 400pt

   Solver definition file structure

Now make sure the solver definition file is arranged correctly.

Launch iRIC. The [iRIC Start Page] dialog
( :numref:`iric_start_dialog_for_solverdef` ) is shown, so
please click on [New Project]. The [Solver Select] dialog
(:numref:`solver_select_dialog_for_solverdef` )
will open, so make sure if there is a new item \"Sample Solver\" in the
solver list. When you find it, select it and make sure that the basic
information of the solver you wrote in solver definition file is shown.

Please note that the following attributes are not shown on this dialog:

-  name
-  executable
-  iterationtype
-  gridtype

.. _iric_start_dialog_for_solverdef:

.. figure:: images/iric_start_dialog.png
   :width: 320pt

   The [iRIC Start Page] dialog

.. _solver_select_dialog_for_solverdef:

.. figure:: images/solver_select_dialog.png
   :width: 350pt

   The [Select Solver] dialog

You sould take care about name attribute and version attribute, when you
want to update a solver. Please refer to :ref:`notice_about_version` for the detail.
