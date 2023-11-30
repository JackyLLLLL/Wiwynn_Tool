# import yaml
from pyModbusTCP.client import ModbusClient

name = "T08"
ipaddress = "172.22.199.250"
port = 502

secondary_flow_rate_ctrl = 6096 #寫入水流的寄存器地址
input_flow_value_to_write = 85 #要寫入的值 80-90 填寫水流 先用 80 測試 (80 轉800(x10倍)轉16進位)
secondary_tsupply_ctrl = 6098 #寫入溫度的寄存器地址
input_tsupply_value_to_write = 25 #要寫入的值 20-25 填寫溫度 先用 20 測試 (20 轉800(x10倍)轉16進位)
auto_ctrl_switch = 2048

# flow_value_to_write = hex(flow_value_to_write * 10)[2:]
# tsupply_value_to_write = hex(tsupply_value_to_write * 10)[2:]

flow_value_to_write  = input_flow_value_to_write * 10
tsupply_value_to_write = input_tsupply_value_to_write * 10


c = ModbusClient(host=ipaddress, port=port,auto_open=True, auto_close=True,timeout=0.2)

# Function 6: Write single holding register
c.write_single_register(secondary_flow_rate_ctrl, flow_value_to_write)
print(f"測試寫入地址:{secondary_flow_rate_ctrl},測試寫入水流值:{input_flow_value_to_write}(LPM)")

# Function 6: Write single holding register
c.write_single_register(secondary_tsupply_ctrl, tsupply_value_to_write)
print(f"測試寫入地址:{secondary_tsupply_ctrl},測試寫入溫度值:{input_tsupply_value_to_write}度C")

# Function 5: Write single coil
c.write_single_coil(auto_ctrl_switch, True)
print(f"Auto Ctrl. Switch:Control Start,auto_ctrl_switch:{auto_ctrl_switch}")
print("finish")


