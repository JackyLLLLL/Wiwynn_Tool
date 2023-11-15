from datetime import datetime, timedelta

log_path = r"C:\Users\11203638\Desktop\idle_time_data\Monica\C41A8_Gen2\M1289073902P3312000206E\M1289073902P3312000206E_history.log"

name_idle_times = {}
previous_end_time = None

with open(log_path, 'r') as file:
    header = file.readline().split()

    # Determine log format based on header
    if 'Stage' in header and 'Result' in header:
        log_format = "format1"
    elif 'TP_POWER_ON' in header:
        log_format = "format2"
    else:
        raise ValueError("Unsupported log format")

    for line in file:
        parts = line.split()

        if log_format == "format1":
            if len(parts) >= 9:
                _, stage, name, start_day, start_time, end_day, end_time, _, _ = parts
                start_time = datetime.strptime(start_day + " " + start_time, '%Y-%m-%d %H:%M:%S')
                end_time = datetime.strptime(end_day + " " + end_time, '%Y-%m-%d %H:%M:%S')

                # Calculate IDLE TIME for each NAME
                if previous_end_time is not None :
                    idle_time = start_time - previous_end_time
                    # Update or initialize the total IDLE TIME for this NAME
                    name_idle_times[name] = name_idle_times.get(name, timedelta()) + idle_time
    
                previous_end_time = end_time

            else:
                print(f"Unsupported log format in line: {line}")
                continue

        elif log_format == "format2":
            if len(parts) >= 9:
                _, stage, name, start_time_str, end_time_str, _, _, _, _ = parts
                start_time = datetime.strptime(start_time_str, '%Y%m%d_%H:%M:%S')
                end_time = datetime.strptime(end_time_str, '%Y%m%d_%H:%M:%S')

                # Calculate IDLE TIME for each NAME
                if previous_end_time is not None and 'IDLE' in stage:
                    idle_time = start_time - previous_end_time

                    # Update or initialize the total IDLE TIME for this NAME
                    name_idle_times[name] = name_idle_times.get(name, timedelta()) + idle_time

                previous_end_time = end_time

            else:
                print(f"Unsupported log format in line: {line}")
                continue

# Print results
for name, idle_time in name_idle_times.items():
    print(f"{name} IDLE Time: {idle_time}")