
#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("=====program Start=====")

count = range(1,500)

for count in count:
    
    file_path = (r"C:\Users\11203638\Desktop\sensor_log\sensor_%d.txt"%count)

    

    
    with open (file_path, "r") as f:
        data = f.read()

        if  "Temp_HD_0 = 00 Init" in data:
            #確認Temp_HD_0 = 00 Init有在檔案內
            print(file_path)
            print(data)



print("=====program End=====")
