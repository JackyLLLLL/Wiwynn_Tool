import re
#0123456789ABCDEF
#1234.5678.9ABC
#12:34:56:78:9A:BC
#123456789ABC
#1234-5678-9ABC

mac_1 = "1e:57:dc:d5:0a:65"
#       fe80::1c57:dcff:fed5:0a65


mac_2 = "82:07:e8:00:a7:d3"
#	fe80::8007:e8ff:fe00:a7d3


mac_3 =	"52:5e:37:63:a1:1b"
#	fe80::505e:37ff:fe63:a11b

while True:
    # pattern = r'^[0-9a-f]{12}$'

    mac_address = input("請輸入MAC地址:")
    mac_address = mac_address.lower()


    # if re.match(pattern,mac_address):
    #     print("正確的MAC格式",mac_address)
    #     break
    # else:
    #     print("字元錯誤或不正確的MAC地址長度")

    MAC_before_calculation = re.sub(r'[^0-9a-f]+', '', mac_address)
    if len(MAC_before_calculation) == 12:
        print("正確的MAC格式",MAC_before_calculation)
        break
    else:
        print("字元錯誤或不正確的MAC地址長度")


print(MAC_before_calculation)

def hex_to_bin(self):
    self = self[0]+self[1] 
    self = bin(int(self,16))[2:].zfill(8) #使用了.zfill(8)方法，在二進位表示的前面填充足夠的零位元，確保輸出是8個位元
    return self

bin_mac = hex_to_bin(MAC_before_calculation)
#print("尚未反轉第七位的:",bin_mac)
seventh_digit = bin_mac[6] #八個位組的取出第七位位組

if seventh_digit == "1":
    seventh_digit = bin_mac[6].replace("1","0")
    #print("確認第七位為1，反轉為:",seventh_digit)
else:
    seventh_digit = bin_mac[6].replace("0","1")
    #print("確認第七位為0，反轉為:",seventh_digit)

#print("已經反轉第七位的:",bin_mac[:6]+seventh_digit+bin_mac[-1])
new_bin_mac = bin_mac[:6]+seventh_digit+bin_mac[-1] #將已反轉第七位的位組存到變數
hexadecimal = hex(int(new_bin_mac,2))[2:] #將二進位轉回十六進位

ipv6_address = (f"fe80::{hexadecimal}{MAC_before_calculation[2:4]}:{MAC_before_calculation[4:6]}ff:fe{MAC_before_calculation[6:8]}:{MAC_before_calculation[8:]}")

print(f"轉出來的ipv6 link local address_ {ipv6_address}")


# bin_mac = hex_to_bin(MAC_before_calculation) #引用function 十六進位轉二進位
# print("尚未反轉第七位的:",bin_mac)

# seventh_digit = bin_mac[6] #八個位組的取出第七位位組

# if seventh_digit == "1":
#     seventh_digit = bin_mac[6].replace("1","0")
#     print("確認第七位為1，反轉為:",seventh_digit)
# else:
#     seventh_digit = bin_mac[6].replace("0","1")
#     print("確認第七位為0，反轉為:",seventh_digit)


# print("已經反轉第七位的:",bin_mac[:6]+seventh_digit+bin_mac[-1])
# new_bin_mac = bin_mac[:6]+seventh_digit+bin_mac[-1] #將已反轉第七位的位組存到變數
# hexadecimal = hex(int(new_bin_mac,2))[2:] #將二進位轉回十六進位
# ipv6_address = MAC_before_calculation.split(":")
# ipv6_address[0] = hexadecimal
# ipv6_address.insert(3,"ff")
# ipv6_address.insert(4,"fe")
# ipv6_address.insert(0,"fe80::")

# ipv6_address_result = ipv6_address[0]+ipv6_address[1]+ipv6_address[2]+":"+ipv6_address[3]+ipv6_address[4]+":"+ipv6_address[5]+ipv6_address[6]+":"+ipv6_address[7]+ipv6_address[8]
# print("MAC adderss:",MAC_before_calculation)
# print("IPv6 address:",ipv6_address_result)



    











