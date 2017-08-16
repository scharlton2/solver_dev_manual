.. _calccond_def_examples:

Examples of calculation conditions, boundary conditions, and grid generating condition
---------------------------------------------------------------------------------------

Example of definitions of calculating conditions in solver definition
files, grid generating condition if grid generating program definition
file is shown in this section. The position to describe the definition
differs like shown in :numref:`where_to_define_element`,
but the grammers are the same. Refer to
:ref:`def_structure` for the whole structure of each file.

.. _where_to_define_element:

.. csv-table:: Position to define definition elements
   :file: where_to_define_element.csv
   :header-rows: 1

The types of items available, are shown in
:numref:`definition_file_widget_types`. In this
subsection, the followings are described fore each type:

-  Definition example
-  Example of the corresponding widget shown on calculation condition
   edit dialog in iRIC
-  Code example to load the values in solvers (or grid generating
   program).


In code examples to load the values, subroutines in iRIClib are used.
Please refer to :ref:`about_iriclib` to know more about iRIClib.

The examples only
show the sample codes for loading, so please refer to :ref:`how_to_dev_solver`,
:ref:`how_to_dev_gridgen` to see examples of whole programs.

.. _definition_file_widget_types:

.. csv-table:: Types of calculation conditions and grid generating conditions
   :file: widget_types.csv
   :header-rows: 1

.. toctree::
   :maxdepth: 2

   03_01_01_example_string
   03_01_02_example_filename_read
   03_01_03_example_filename_save
   03_01_04_example_foldername
   03_01_05_example_integer
   03_01_06_example_integer_select
   03_01_07_example_real
   03_01_08_example_func
   03_01_09_example_func_multi
