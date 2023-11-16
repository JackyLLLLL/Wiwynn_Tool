#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
from datetime import datetime, timedelta



log_path = r"C:\Users\11203638\Desktop\idle_time_calculate\Monica\C41A8_Gen2\M1289073902P3312000206E\M1289073902P3312000206E_history.log"
# aws_log_path = r"C:\Users\11203638\Desktop\idle_time_calculate\AWS\Teton_Prime_Gen1\WAA5HN34100FL_history.log"
# meta_log_path = r"C:\Users\11203638\Desktop\idle_time_calculate\Meta\BZA04M01001L3390013N1B_history.log"
# meta_log_path = r"C:\Users\11203638\Desktop\idle_time_calculate\Meta\golden.log"

log_path = r"C:\Users\11203638\Desktop\idle_time_calculate\Monica\C41A8_Gen2\M1289073902P3312000206E\test.log"

###########################################
output_filename = fr"Idle_time.csv"
output_file_path = output_filename
counter = 1
while os.path.exists(output_file_path):
    filename, extension = os.path.splitext(output_filename)
    output_file_path = f"{filename}_{counter}{extension}"
    counter += 1
#############################################
previous_end_time = None
total_idle_time = timedelta()
no_idle_time = timedelta()
stage_idle_times = {}


with open(log_path, 'r') as file:
    header = file.readline().split()

    # Determine log format based on header

    if 'Stage' in header and 'Result' in header:
        log_format = "format1"

    elif 'TP_POWER_ON' in header:
        log_format = "format2"

    else:
        raise ValueError("Unsupported log format")

    with open(output_file_path,"w",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID","Stage", "Name","IDLE time"])

    for line in file:
        parts = line.split()

        if log_format == "format1":
            if len(parts) >= 9:
                id, stage, name, start_day, start_time, end_day, end_time, duration, result = parts
                start_time = datetime.strptime(start_day + " " + start_time, '%Y-%m-%d %H:%M:%S')
                end_time = datetime.strptime(end_day + " " + end_time, '%Y-%m-%d %H:%M:%S')
                
                if previous_end_time is None:
                    pass
                else:
                    idle_time = start_time-previous_end_time

                    if idle_time == no_idle_time or idle_time < no_idle_time:
                        pass
                    else:
                      
                        with open(output_file_path,"a",newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([id,stage,name,idle_time])
                        print(f"{id} {stage} {name} {idle_time}")
                        total_idle_time += idle_time

                        if stage in stage_idle_times:
                            stage_idle_times[stage] += idle_time
                        else:
                            stage_idle_times[stage] = idle_time

                previous_end_time = end_time

            else:
                print(f"Unsupported log format in line: {line}")
                continue

        elif log_format == "format2":
            if len(parts) >= 9:
                id, stage, name, start_time_str, end_time_str, _, _, _, result = parts
                start_time = datetime.strptime(start_time_str, '%Y%m%d_%H:%M:%S')
                end_time = datetime.strptime(end_time_str, '%Y%m%d_%H:%M:%S')

                if previous_end_time is None:
                    pass
                else:
                    idle_time = start_time-previous_end_time

                    if idle_time == no_idle_time or idle_time < no_idle_time:
                        pass
                    else:
                        print(f"{id} {stage} {name} {idle_time}")
                        total_idle_time += idle_time

                previous_end_time = end_time

            else:
                print(f"Unsupported log format in line: {line}")
                continue

    # 列印每個 STAGE 的 IDLE 時間總和
    print("Stage IDLE Times:")

with open(output_file_path,"a",newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Stage","IDLE_time"])

for stage, idle_time in stage_idle_times.items():
    
    with open(output_file_path,"a",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([stage,idle_time])
    print(f"{stage}: {idle_time}")

print(f"Total IDLE Time: {total_idle_time}")
print(f"Out Put File name:{output_file_path}")