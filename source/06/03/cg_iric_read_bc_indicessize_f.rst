cg_iric_read_bc_indicessize_f
=============================

境界条件が設定された要素 (格子点もしくはセル) の数を取得する。

形式
----
.. code-block:: fortran

   call cg_iric_read_bc_indicessize_f(type, num, size, ier)

引数
----

.. csv-table:: cg_iric_read_bc_indicessize_f の引数
   :file: cg_iric_read_bc_indicessize_f_args.csv
   :header-rows: 1

備考
----

size に返される値は、境界条件が設定される位置によって、 :numref:`bc_position_and_size` に示すように異なります。

.. _bc_position_and_size:

.. csv-table:: 境界条件を設定された位置と size に返される値の関係
   :file: cg_iric_read_bc_indicessize_position_and_size.csv
   :header-rows: 1

