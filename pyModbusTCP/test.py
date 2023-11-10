#0123456789ABCDEF
#1234.5678.9ABC
#12:34:56:78:9A:BC
#123456789ABC
#1234-5678-9ABC

import re


import re

def validate_string(string):
    pattern = r'^[0-9A-F]{12}$'
    if re.match(pattern, string):
        return True
    else:
        return False

# 測試範例
strings = ["1234ABCD5678", "ABCDEFG123456", "1234567890AB", "1234567890ABCDE"]
for string in strings:
    result = validate_string(string)
    print(f"{string}: {result}")

##while True:
##
##    mac = input("請輸入MAC:")
##
##    mac = mac.lower() 
##    
##    filtered_mac = re.sub(r'[^0-9a-f]+', '', mac)
##
##    if len(filtered_mac) == 12:
##        print("正確",filtered_mac)
##        break
##    else:
##        print("字元錯誤或不正確的MAC地址長度")
