schtasks /create /tn get_wrf_data0 /tr D:\workbyDan\wearther_data\src\get_wrf_weatherdata.bat  /sc daily /st 00:05
schtasks /create /tn get_wrf_data1 /tr D:\workbyDan\wearther_data\src\get_wrf_weatherdata.bat /sc daily /st 06:05
schtasks /create /tn get_wrf_data2 /tr D:\workbyDan\wearther_data\src\get_wrf_weatherdata.bat /sc daily /st 12:05
schtasks /create /tn get_wrf_data3 /tr D:\workbyDan\wearther_data\src\get_wrf_weatherdata.bat /sc daily /st 18:05