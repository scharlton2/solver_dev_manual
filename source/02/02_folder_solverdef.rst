.. _create_solverdef_folder:

Creating a folder
==================

Create a special folder for the solver you develop under the \\"solvers\\"
folder under the installation folder of iRIC. 
This time, please create \\"example\\" folder.

.. _how_to_create_solver_def_file:

Creating a solver definition file
===================================

Create a solver definition file.

In solver definition file, you are going to define the information shown
in :numref:`infos_to_define_in_solverdef`.

.. _infos_to_define_in_solverdef:

.. csv-table:: Informations defined in solver definition file
   :file: infos_to_define_in_solverdef.csv
   :header-rows: 1

Solver definition file is described in XML language. The basic grammer
of XML language is explained in Section 5.6.

In this section, we add definition information of a solver in the order
shown in Table :numref:`infos_to_define_in_solverdef`.

.. toctree::
   :maxdepth: 4

   02_01_solverdef_basic
   02_02_solverdef_calccond
   02_03_solverdef_gridcond
   02_04_solverdef_boundarycond
