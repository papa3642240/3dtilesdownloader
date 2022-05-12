@echo off
title downloader-V20201120.001

@REM downloader.exe --url=http://localhost:5008/shanghai/tileset.json -d  E:\项目集合\三维GIS与数据孪生研究\下载数据\倾斜摄影\3DTiles\EarthBuildingData  -t 3 -s 9 -e 13

@REM downloader.exe --url=http://ts.wish3d.com/zhengwu/shuqian/data/model/zhonghao_new/tileset.json -d  E:\项目集合\三维GIS与数据孪生研究\下载数据\倾斜摄影\3DTiles\EarthBuildingData  -t 3

downloader.exe --url=http://localhost:5200/online-bim/college/3dtiles/bim-daxue/tileset.json -d  D:\cesium-download-data\bim-3dtiles  -t 10
