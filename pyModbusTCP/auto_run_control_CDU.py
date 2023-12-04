# main_program.py
import sys
from modbusCDU_module import ModbusWriter

"""
python3 auto_run.py [ip] [water flow] [temperture]

e.q
python3 auto_run.py 172.22.199.251 85 20

"""


if __name__ == "__main__":
    name = "T08"
    ipaddress = sys.argv[1]
    if len(ipaddress) == 14:
        pass
    else:
        print("ip長度不正確，程式結束")
        sys.exit()

    port = 502
    secondary_flow_rate_ctrl = 6096
    secondary_tsupply_ctrl = 6098
    auto_ctrl_switch = 2048

    input_flow_value_to_write = int(sys.argv[2])
    if 80<=input_flow_value_to_write <= 90:
        pass
    else:
        print("輸入的水流數值不正確，程式結束")
        sys.exit()

    
    input_tsupply_value_to_write = int(sys.argv[3])
    if 20<= input_tsupply_value_to_write <= 25:
        pass
    else:
        print("輸入的溫度數值不正確，程式結束")
        sys.exit()

    modbus_writer = ModbusWriter(ipaddress, port=port)

    flow_value_to_write = input_flow_value_to_write * 10
    tsupply_value_to_write = input_tsupply_value_to_write * 10

    modbus_writer.write_single_register(secondary_flow_rate_ctrl, flow_value_to_write)
    modbus_writer.write_single_register(secondary_tsupply_ctrl, tsupply_value_to_write)
    modbus_writer.write_single_coil(auto_ctrl_switch, True)

    print("完成寫入操作")