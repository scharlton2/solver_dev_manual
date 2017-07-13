Abstract
==========

Solver is a program that load grid and calculation conditions, execute a
river simulation, and output calculation results.

To add a solver to iRIC, it is necessary to make and deploy files shown
in :numref:`files_related_to_solver`.

Solver developers have to create a new folder under "solvers" folder under
iRIC install folder, and deploy files in :numref:`files_related_to_solver`
that you've prepared for your new solver.

.. _files_related_to_solver:

.. csv-table:: Files related to a Solver
   :file: files_related_to_solver.csv
   :header-rows: 1

Abstracts of each file are as follows:

definition.xml
--------------

File that defines the following information of solvers:

- Basic Information
- Calculation Conditions
- Grid Attributes

iRIC loads definition xml, and provides interface for creating
calculation conditions and grids that can be used by the solver. Solver
definition file should be written in English.


Solver
--------

Executable module of a river simulation solver. It loads calculation
condition and grids created using iRIC, executes river simulation, and
outputs result.

Solvers use calculation data files created by iRIC, for loading and
writing calculation condition, grids, and calculation results. Solvers
can also use arbitrary files for data I/O that cannot be loaded from or
written into calculation data files.

Solvers can be developed using FORTRAN, C or C++. In this chapter, a
sample solver is developed in FORTRAN.

translation\_ja\_JP.ts etc.
---------------------------

Dictionary files for a solver definition file. It provides translation
information for texts shown on dialogs or object browser in iRIC.
Dictionary files are created as separate files for each language.
For example, "translation\_ja\_JP.ts" for Japanese, "translation\_ka\_KR.ts"
for Korean.


README
------

README is a text file that describes about the solver. The content of
README is shown in the "Description" tab in the [Select Solver] dialog.

LICENSE
-------

LICENSE is a text file that describes about the license of the solver.
The content of LICENSE is shown in the "License" tab in the
[Select Solver] dialog.

:numref:`relations_between_solver_and_files` shows the relationships of
iRIC, solver and related files.

.. _relations_between_solver_and_files:

.. figure:: images/files_related_to_solver.png

   Relationships between iRIC, solvers, and related files

This chapter explains the steps to create the files described in this
section.
