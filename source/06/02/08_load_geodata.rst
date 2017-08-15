地形データの読み込み
======================

プロジェクトでインポートして格子生成に利用した地形データを読み込みます。
ソルバーで、河川測量データやポリゴンを直接読み込んで解析に使用したい場合に行います。
地形データを読み込む場合の手順は、以下の通りになります。

1. CGNS ファイルから、プロジェクトで使用した地形データのファイル名などを読み込みます。
2. 地形データファイルを開き、地形データを読み込みます。

.. list-table:: 利用する関数
   :header-rows: 1

   * - 関数
     - 備考
   * - cg_iric_read_geo_count_f
     - 地形データの数を返す
   * - cg_iric_read_geo_filename_f
     - 地形データのファイル名と種類を返す
   * - iric_geo_polygon_open_f
     - ポリゴンファイルを開く
   * - iric_geo_polygon_read_integervalue_f
     - ポリゴンの値を整数で返す
   * - iric_geo_polygon_read_realvalue_f
     - ポリゴンの値を実数で返す
   * - iric_geo_polygon_read_pointcount_f
     - ポリゴンの頂点の数を返す
   * - iric_geo_polygon_read_points_f
     - ポリゴンの頂点の座標を返す
   * - iric_geo_polygon_read_holecount_f
     - ポリゴンに開いた穴の数を返す
   * - iric_geo_polygon_read_holepointcount_f
     - ポリゴンの穴の頂点の数を返す
   * - iric_geo_polygon_read_holepoints_f
     - ポリゴンの穴の頂点の座標を返す
   * - iric_geo_polygon_close_f
     - ポリゴンファイルを閉じる
   * - iric_geo_riversurvey_open_f
     - 河川測量データを開く
   * - iric_geo_riversurvey_read_count_f
     - 河川横断線の数を返す
   * - iric_geo_riversurvey_read_position_f
     - 横断線の中心点の座標を返す
   * - iric_geo_riversurvey_read_direction_f
     - 横断線の向きを返す
   * - iric_geo_riversurvey_read_name_f
     - 横断線の名前を文字列として返す
   * - iric_geo_riversurvey_read_realname_f
     - 横断線の名前を実数値として返す
   * - iric_geo_riversurvey_read_leftshift_f
     - 横断線の標高データのシフト量を返す
   * - iric_geo_riversurvey_read_altitudecount_f
     - 横断線の標高データの数を返す
   * - iric_geo_riversurvey_read_altitudes_f
     - 横断線の標高データを返す
   * - iric_geo_riversurvey_read_fixedpointl_f
     - 横断線の左岸延長線のデータを返す
   * - iric_geo_riversurvey_read_fixedpointr_f
     - 横断線の右岸延長線のデータを返す
   * - iric_geo_riversurvey_read_watersurfaceelevation_f
     - 横断線での水面標高のデータを返す
   * - iric_geo_riversurvey_close_f
     - 河川測量データを閉じる

地形データのうち、ポリゴンを読み込む処理の記述例を
:numref:`example_load_polygon` に、
河川測量データを読み込む処理の記述例を :numref:`example_load_riversurvey`
にそれぞれ示します。

.. code-block:: fortran
   :caption: ポリゴンを読み込む処理の記述例
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
   
   
     ! 計算データファイルを開く
     call cg_open_f("test.cgn", CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! iRIClib の初期化
     call cg_iric_init_f(fin, ier)
   
     ! 地形データの数を取得
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
   
     ! 計算データファイルを閉じる
     call cg_close_f(fin, ier)
     stop
   end program TestPolygon

.. code-block:: fortran
   :caption: 河川測量データを読み込む処理の記述例
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
   
     ! 計算データファイルを開く
     call cg_open_f("test.cgn", CG_MODE_MODIFY, fin, ier)
     if (ier /=0) stop "*** Open error of CGNS file ***"
   
     ! iRIClib の初期化
     call cg_iric_init_f(fin, ier)
   
     ! 地形データの数を取得
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
   
     ! 計算データファイルを閉じる
     call cg_close_f(fin, ier)
     stop
   end program TestRiverSurvey

