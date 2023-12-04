import sys
from pyModbusTCP.client import ModbusClient

class ModbusWriter:
    def __init__(self, ipaddress, port=502, timeout=0.2):
        self.ipaddress = ipaddress
        self.port = port
        self.timeout = timeout
        self.c = ModbusClient(host=self.ipaddress, port=self.port, auto_open=True, auto_close=True, timeout=self.timeout)

    def write_single_register(self, register_address, value):
        try:
            self.c.write_single_register(register_address, value)
            #print(f"寫入地址:{register_address}, 寫入數值:{value}")
        except Exception as e:
            print(f"寫入時發生錯誤: {str(e)}")

    def write_single_coil(self, coil_address, value):
        try:
            self.c.write_single_coil(coil_address, value)
            #print(f"寫入 Coil 地址:{coil_address}, 寫入數值:{value}")
        except Exception as e:
            print(f"寫入 Coil 時發生錯誤: {str(e)}")