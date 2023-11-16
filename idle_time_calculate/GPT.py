#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
from datetime import datetime, timedelta

log_path = r"C:\Users\11203638\Desktop\idle_time_calculate\Monica\C41A8_Gen2\M1289073902P3312000206E\M1289073902P3312000206E_history.log"
output_filename = fr"Idle_time.csv"

# 生成輸出文件路徑
base_path = os.path.dirname(os.path.realpath(__file__))
output_file_path = os.path.join(base_path, output_filename)
counter = 1
while os.path.exists(output_file_path):
    filename, extension = os.path.splitext(output_filename)
    output_file_path = f"{filename}_{counter}{extension}"
    counter += 1

previous_end_time = None
total_idle_time = timedelta()
no_idle_time = timedelta()
stage_idle_times = {}

with open(log_path, 'r') as file:
    header = file.readline().split()

    # 確定日誌格式
    if 'Stage' in header and 'Result' in header:
        log_format = "format1"
    elif 'TP_POWER_ON' in header:
        log_format = "format2"
    else:
        raise ValueError("Unsupported log format")

    # 寫入 CSV 標頭
    with open(output_file_path, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Stage", "Name", "IDLE time"])

    for line in file:
        parts = line.split()

        if log_format == "format1":
            if len(parts) >= 9:
                id, stage, name, start_day, start_time, end_day, end_time, duration, result = parts
                start_time = datetime.strptime(start_day + " " + start_time, '%Y-%m-%d %H:%M:%S')
                end_time = datetime.strptime(end_day + " " + end_time, '%Y-%m-%d %H:%M:%S')

                if previous_end_time is not None:
                    idle_time = start_time - previous_end_time

                    if idle_time != no_idle_time and idle_time > no_idle_time:
                        with open(output_file_path, "a", newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([id, stage, name, str(idle_time)])
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

                if previous_end_time is not None:
                    idle_time = start_time - previous_end_time

                    if idle_time != no_idle_time and idle_time > no_idle_time:
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

print(f"Total IDLE Time: {total_idle_time}")

# 列印每個 STAGE 的 IDLE 時間總和
print("Stage IDLE Times:")
for stage, idle_time in stage_idle_times.items():
    print(f"{stage}: {idle_time}")