@echo off
echo Bat start

D:
cd D:\workbyDan\wearther_data\src
call activate weather_API
python get_wrf_weatherdata.py
call conda deactivate
exit