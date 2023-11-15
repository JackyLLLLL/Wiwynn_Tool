import yaml
from pyModbusTCP.client import ModbusClient

yaml_path = r"/home/jackywnlin/mnt_jacky_link/pyModbusTCP/CDU_ip.yaml"


#2059-2066 range=1

with open (yaml_path,"r",encoding="utf-8") as file:
    cfg = yaml.load(file,Loader=yaml.FullLoader)
    


    for tank_id in cfg:

        name = cfg[tank_id]["name"]
        ipaddress = cfg[tank_id]["ipaddress"]
        port = cfg[tank_id]["port"]
        address = cfg[tank_id]["address"]
        Range = cfg[tank_id]["range"]

        # TCP auto connect on first modbus request
        c = ModbusClient(host=ipaddress, port=port, auto_open=True, auto_close=True)
        # Address: 4096 , bit: 1x16 bit
        
        s = c.read_holding_registers(address, Range)
        
        z = []

        for s in s:
         s = s * 0.1
         z.append('%.1f'%s)

        try:
            z.insert(0,name)
            #x= [name] + s
            
            for read_bool in range(2059,2067):
                x = c.read_discrete_inputs(read_bool,1)
                z.append(x)
            
            print(z)

        except AttributeError :
            print(f"Error,{name},ip:{ipaddress}")


