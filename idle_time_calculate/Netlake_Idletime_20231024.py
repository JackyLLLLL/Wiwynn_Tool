import os
import numpy as np
from datetime import datetime, date,timedelta


log_path = r"C:\Users\11203638\Desktop\idle_time_data\Monica\C41A8_Gen2\M1289073902P3312000206E\M1289073902P3312000206E_history.log"
log_path = r"C:\Users\11203638\Desktop\idle_time_data\Meta\BZA04M01001L3390013N1B_history.log"
#打開golden檔
f = open(log_path,'r+')
line = f.readlines()

#刪除line1,line2
del line[0]
del line[0]

#找空元素
line_num = 0
del_line = []

for i in line:
    teststr = i.split()
    if len(teststr) == 0 :
        del_line.append(line_num)
    line_num = line_num + 1

#刪除空元素
for i in range(len(del_line)-1,-1,-1):
    num = del_line[i]
    del line[num]

#找剩餘計算行數
line_counter=0

for i in line:
    line_counter=line_counter+1

#抓取計算時間存在list
line1=[]
for i in range(0,line_counter,1):
    teststr = line[i].split()
    StartA = teststr[3]+ ' ' +teststr[4]
    EndA = teststr[5]+ ' ' +teststr[6]
    line1.append(StartA)
    line1.append(EndA)

#initial time
differencetime = timedelta()
total_time_str = '0000-00-00 00:00:00'
total_time_struct = timedelta()
for i in range(0,line_counter-1,1):
    time1_struct = datetime.strptime(line1[2*i+1], "%Y-%m-%d %H:%M:%S")
    time2_struct = datetime.strptime(line1[2*i+2], "%Y-%m-%d %H:%M:%S")

    if(time1_struct > time2_struct):
        print(" ")
    else:
        differencetime = time2_struct - time1_struct
    total_time_struct = total_time_struct + differencetime
    print("1",total_time_struct)
print("Idletime:", total_time_struct)

f.close()


