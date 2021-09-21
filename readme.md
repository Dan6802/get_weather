***********************************************************************************
抓取氣象資料平台資料
來源:https://opendata.cwb.gov.tw

請先安裝好環境需要套件
*BeautifulSoup
*python 3.6 版以上

conda create -n weather_API

第一步 修改批次檔案:
get_wrf_weatherdata.bat 修改工作目錄與啟動環境

第二步 修改執行檔:
get_wrf_weatherdata.py 設定 main_directory 到自己要的檔案

第三部 建立排程:
set_schedule.bat 設定 batfile 到 get_wrf_weatherdata.py 檔案的絕對路徑

以上都設定完後執行 set_schedule.bat 就完成了

系統將會在每天 00:05 06:05 12:05 18:05 這些時間點自動去抓資料

如果要解除排程只需要執行 del_schedule.bat

Create By Dan 2021_8_17

**********************************************************************************