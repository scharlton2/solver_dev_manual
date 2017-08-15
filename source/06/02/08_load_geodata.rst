Reading geographic data
============================

Reads geographic data that was imported into project and used for grid generation.

This function is used when you want to read river survey data or
polygon data in solvers directly.
The procedure of reading geographic data is as follows:

1. Reads the number of geographic data, the file name of geographic data etc. from CGNS file.
2. Open geographic data file and read data from that.

.. list-table:: Subroutine to use
   :header-rows: 1

   * - Subroutine
     - Remarks
   * - cg_iric_read_geo_count_f
     - Reads the number of geographic data
   * - cg_iric_read_geo_filename_f
     - Reads the file name and data type of geographic data
   * - iric_geo_polygon_open_f
     - Opens the geographic data file that contains polygon data
   * - iric_geo_polygon_read_integervalue_f
     - Reads the value of polygon data as integer
   * - iric_geo_polygon_read_realvalue_f
     - Reads the value of polygon datas double precision real
   * - iric_geo_polygon_read_pointcount_f
     - Reads the number of polygon vertices
   * - iric_geo_polygon_read_points_f
     - Reads the coorinates of polygon vertices
   * - iric_geo_polygon_read_holecount_f
     - Reads the number of holes in the polygon
   * - iric_geo_polygon_read_holepointcount_f
     - Reads the number of vertices of hole polygon
   * - iric_geo_polygon_read_holepoints_f
     - Reads the coordinates of hole polygon vertices
   * - iric_geo_polygon_close_f
     - Closes the geographic data file
   * - iric_geo_riversurvey_open_f
     - Opens the geographic data file that contains river survey data
   * - iric_geo_riversurvey_read_count_f
     - Reads the number of the crosssections in river survey data
   * - iric_geo_riversurvey_read_position_f
     - Reads the coordinates of the crosssection center point
   * - iric_geo_riversurvey_read_direction_f
     - Reads the direction of the crosssection as normalized vector
   * - iric_geo_riversurvey_read_name_f
     - Reads the name of the crosssection as string
   * - iric_geo_riversurvey_read_realname_f
     - Reads the name of the crosssection as real number
   * - iric_geo_riversurvey_read_leftshift_f
     - Reads the shift offset value of the crosssection
   * - iric_geo_riversurvey_read_altitudecount_f
     - Reads the number of altitude data of the crosssection
   * - iric_geo_riversurvey_read_altitudes_f
     - Reads the altitude data of the crosssection
   * - iric_geo_riversurvey_read_fixedpointl_f
     - Reads the data of left bank extension line of the crosssection
   * - iric_geo_riversurvey_read_fixedpointr_f
     - Reads the data of right bank extension line of the crosssection
   * - iric_geo_riversurvey_read_watersurfaceelevation_f
     - Reads the water elevation at the crosssection
   * - iric_geo_riversurvey_close_f
     - Closes the geographic data file

:numref:`example_load_polygon` shows an example of reading polygon.
:numref:`example_load_riversurvey` shows an example of reading river survey data. 

.. code-block:: fortran
   :caption: Example source code of reading polygon
   :name: example_load_polygon
   :linenos:

   program TestPolygon
     implicit none
     include 'cgnslib_f.h'
     include 'iriclib_f.h'
     integer:: fin, ier
     integer:: icount, istatus
   
     integer:: geoid
     integer:: elevation_geo_count
     character(len=1000):: filename
     integer:: geotype
     integer:: polygonid
     double precision:: polygon_value
     integer:: region_pointcount
     double precision, dimension(:), allocatable:: region_pointx
     double precision, dimension(:), allocatable:: region_pointy
     integer:: hole_id
     integer:: hole_count
     integer:: hole_pointcount
     double precision, dimension(:), allocatable:: hole_pointx
     double precision, dimension(:), allocatable:: hole_pointy
   
   
     ! Opens CGNS file
     call cg_open_f("test.cgn", CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! Initializes iRIClib
     call cg_iric_init_f(fin, ier)
   
     ! Reads the number or geographic data
     call cg_iric_read_geo_count_f("Elevation", elevation_geo_count, ier)
   
     do geoid = 1, elevation_geo_count
       call cg_iric_read_geo_filename_f('Elevation', geoid, &
         filename, geotype, ier)
       if (geotype .eq. iRIC_GEO_POLYGON) then
         call iric_geo_polygon_open_f(filename, polygonid, ier)
         call iric_geo_polygon_read_realvalue_f(polygonid, polygon_value, ier)
         print *, polygon_value
         call iric_geo_polygon_read_pointcount_f(polygonid, region_pointcount, ier)
         allocate(region_pointx(region_pointcount))
         allocate(region_pointy(region_pointcount))
         call iric_geo_polygon_read_points_f(polygonid, region_pointx, region_pointy, ier)
         print *, 'region_x: ', region_pointx
         print *, 'region_y: ', region_pointy
         deallocate(region_pointx)
         deallocate(region_pointy)
         call iric_geo_polygon_read_holecount_f(polygonid, hole_count, ier)
         print *, 'hole count: ', hole_count
         do hole_id = 1, hole_count
           print *, 'hole ', hole_id
           call iric_geo_polygon_read_holepointcount_f(polygonid, hole_id, hole_pointcount, ier)
           print *, 'hole pointcount: ', hole_pointcount
           allocate(hole_pointx(hole_pointcount))
           allocate(hole_pointy(hole_pointcount))
           call iric_geo_polygon_read_holepoints_f(polygonid, hole_id, hole_pointx, hole_pointy, ier)
           print *, 'hole_x: ', hole_pointx
           print *, 'hole_y: ', hole_pointy
           deallocate(hole_pointx)
           deallocate(hole_pointy)
         end do
         call iric_geo_polygon_close_f(polygonid, ier)
       end if
     end do
   
     ! Closes CGNS file
     call cg_close_f(fin, ier)
     stop
   end program TestPolygon

.. code-block:: fortran
   :caption: Example source code of reading river survey data
   :name: example_load_riversurvey
   :linenos:

   program TestRiverSurvey
     implicit none
     include 'cgnslib_f.h'
     include 'iriclib_f.h'
     integer:: fin, ier
     integer:: icount, istatus
   
     integer:: geoid
     integer:: elevation_geo_count
     character(len=1000):: filename
     integer:: geotype
     integer:: rsid
     integer:: xsec_count
     integer:: xsec_id
     character(len=20):: xsec_name
     double precision:: xsec_x
     double precision:: xsec_y
     integer:: xsec_set
     integer:: xsec_index
     double precision:: xsec_leftshift
     integer:: xsec_altid
     integer:: xsec_altcount
     double precision, dimension(:), allocatable:: xsec_altpos
     double precision, dimension(:), allocatable:: xsec_altheight
     integer, dimension(:), allocatable:: xsec_altactive
     double precision:: xsec_wse
   
     ! Opens CGNS file
     call cg_open_f("test.cgn", CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! Initializes iRIClib
     call cg_iric_init_f(fin, ier)
   
     ! Reads the number or geographic data
     call cg_iric_read_geo_count_f("Elevation", elevation_geo_count, ier)
   
     do geoid = 1, elevation_geo_count
       call cg_iric_read_geo_filename_f('Elevation', geoid, &
         filename, geotype, ier)
       if (geotype .eq. iRIC_GEO_RIVERSURVEY) then
         call iric_geo_riversurvey_open_f(filename, rsid, ier)
         call iric_geo_riversurvey_read_count_f(rsid, xsec_count, ier)
         do xsec_id = 1, xsec_count
           call iric_geo_riversurvey_read_name_f(rsid, xsec_id, xsec_name, ier)
           print *, 'xsec ', xsec_name
           call iric_geo_riversurvey_read_position_f(rsid, xsec_id, xsec_x, xsec_y, ier)
           print *, 'position: ', xsec_x, xsec_y
           call iric_geo_riversurvey_read_direction_f(rsid, xsec_id, xsec_x, xsec_y, ier)
           print *, 'direction: ', xsec_x, xsec_y
           call iric_geo_riversurvey_read_leftshift_f(rsid, xsec_id, xsec_leftshift, ier)
           print *, 'leftshift: ', xsec_leftshift
           call iric_geo_riversurvey_read_altitudecount_f(rsid, xsec_id, xsec_altcount, ier)
           print *, 'altitude count: ', xsec_altcount
           allocate(xsec_altpos(xsec_altcount))
           allocate(xsec_altheight(xsec_altcount))
           allocate(xsec_altactive(xsec_altcount))
           call iric_geo_riversurvey_read_altitudes_f( &
             rsid, xsec_id, xsec_altpos, xsec_altheight, xsec_altactive, ier)
           do xsec_altid = 1, xsec_altcount
             print *, 'Altitude ', xsec_altid, ': ', &
               xsec_altpos(xsec_altid:xsec_altid), ', ', &
               xsec_altheight(xsec_altid:xsec_altid), ', ', &
               xsec_altactive(xsec_altid:xsec_altid)
           end do
           deallocate(xsec_altpos, xsec_altheight, xsec_altactive)
           call iric_geo_riversurvey_read_fixedpointl_f( &
             rsid, xsec_id, xsec_set, xsec_x, xsec_y, xsec_index, ier)
           print *, 'FixedPointL: ', xsec_set, xsec_x, xsec_y, xsec_index
           call iric_geo_riversurvey_read_fixedpointr_f( &
             rsid, xsec_id, xsec_set, xsec_x, xsec_y, xsec_index, ier)
           print *, 'FixedPointR: ', xsec_set, xsec_x, xsec_y, xsec_index
           call iric_geo_riversurvey_read_watersurfaceelevation_f( &
             rsid, xsec_id, xsec_set, xsec_wse, ier)
           print *, 'WaterSurfaceElevation: ', xsec_set, xsec_wse
         end do
         call iric_geo_riversurvey_close_f(rsid, ier)
       end if
     end do
   
     ! Closes CGNS file
     call cg_close_f(fin, ier)
     stop
   end program TestRiverSurvey
