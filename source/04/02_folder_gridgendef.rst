.. _create_gridgen_folder:

Creating a folder
==================

Create a special folder for the grid generating program you develop
under \\"solvers\\" folder under the installation folder of iRIC.
This time, please create \\"example\\" folder.

.. _how_to_create_gridgen_def_file:

Creating a grid generating program definition file
====================================================

Create a grid generating program definition file.

In grid generating program definition file, you are going to define the
information shown in :numref:`infos_to_define_in_gridgendef`.

.. _infos_to_define_in_gridgendef:

.. csv-table:: Information defined in grid generating program definition file
   :file: infos_to_define_in_gridgendef.csv
   :header-rows: 1

Grid generating program definition file is described in XML language.
The basic grammer of XML language is explained in :ref:`xml_basics`.

In this section, we add definition information of a grid generating
program in the order shown in :numref:`infos_to_define_in_gridgendef`.

.. toctree::
   :maxdepth: 4

   02_01_gridgendef_basic
   02_02_gridgendef_gridgencond
   02_03_gridgendef_errorcode
