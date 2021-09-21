import datetime
import os
import urllib.request
import time

def Download_auto(wrf_dir, wrf_dir2): 
    print("M-A0064")
    i = 0
    while True:        
        try: 
            if i > 84:
                break
            t = "%03d" % i
            file_name = "M-A0064-{}.grb2".format(t)
            res ="https://opendata.cwb.gov.tw/fileapi/opendata/MIC/{}".format(file_name)
            urllib.request.urlretrieve(res,"{}/{}".format(wrf_dir2, file_name))
            i+=6
            if not(i%18):
                print(".")
        except :
            if i>0:
                i=i-6
            print("x")
    print("M-A0061")
    i = 0
    while True:
        try: 
            if i > 84:
                break
            t = "%03d" % i
            file_name = "M-A0061-{}.grb2".format(t)
            res ="https://opendata.cwb.gov.tw/fileapi/opendata/MIC/{}".format(file_name)
            urllib.request.urlretrieve(res,"{}/{}".format(wrf_dir, file_name))
            i+=6
            if not(i%18):
                print(".")
        except :
            if i>0:
                i=i-6
            print("x")

print("Start get wearther data.")
start = time.time()

#set data directory
main_directory = "D:\workbyDan/wearther_data/WRF"
main_directory2 = "D:\workbyDan/wearther_data/WRF2"

if not os.path.exists(main_directory):
    os.mkdir(main_directory)

if not os.path.exists(main_directory2):
    os.mkdir(main_directory2)

today = datetime.datetime.now()
wrf_dir = main_directory + "/{}_{}_{}_{}".format(today.year, today.month, today.day, today.hour)
wrf_dir2 = main_directory2 + "/{}_{}_{}_{}".format(today.year, today.month, today.day, today.hour)

if not os.path.exists(wrf_dir):
    os.mkdir(wrf_dir)

if not os.path.exists(wrf_dir2):
    os.mkdir(wrf_dir2)

Download_auto(wrf_dir, wrf_dir2)

# for i in range(0, 85,6):
#     t = "%03d" % i
#     file_name = "M-A0061-{}.grb2".format(t)
#     res ="https://opendata.cwb.gov.tw/fileapi/opendata/MIC/{}".format(file_name)
#     urllib.request.urlretrieve(res,"{}/{}".format(wrf_dir, file_name))

print("Finish")
print(time.time() - start)