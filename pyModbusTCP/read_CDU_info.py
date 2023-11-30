import yaml
from pyModbusTCP.client import ModbusClient

yaml_path = "/home/jackywnlin/mnt_jacky_link/pyModbusTCP/CDU_info.yaml"


with open (yaml_path,"r",encoding="utf-8") as file:
    cfg = yaml.load(file,Loader=yaml.FullLoader)

    for tank_id in cfg:

        name = cfg[tank_id]["name"]
        ipaddress = cfg[tank_id]["ipaddress"]
        port = cfg[tank_id]["port"]
        secondary_flow_rate = cfg[tank_id]["Secondary Flow Rate"]
        secondary_treturn = cfg[tank_id]["Secondary Treturn"]
        secondary_tsupply = cfg[tank_id]["Secondary Tsupply"]
        primary_tinlet = cfg[tank_id]["Primary Tinlet"]
        primary_pinlet = cfg[tank_id]["Primary Pinlet"]
        ta = cfg[tank_id]["Ta"]
        r_humidity = cfg[tank_id]["R. Humidity"]
        dew_point = cfg[tank_id]["Dew Point"]
        remove_heat = cfg[tank_id]["Remove Heat"]
        pump_output = cfg[tank_id]["Pump Output"]
        cooling = cfg[tank_id]["Cooling"]

        Alert_Secondary_Tsupply = cfg[tank_id]["Alert_Secondary Tsupply"]
        Alert_Primary_Tinlet = cfg[tank_id]["Alert_Primary Tinlet"]
        Alert_Primary_Pinlet = cfg[tank_id]["Alert_Primary Pinlet"]
        Alert_Leakage = cfg[tank_id]["Alert_Leakage"]
        Alert_Fan_Status = cfg[tank_id]["Alert_Fan Status"]
        Alert_Liquid_High = cfg[tank_id]["Alert_Liquid High"]
        Alert_Liquid_Low = cfg[tank_id]["Alert_Liquid Low"]
        Alert_Pump_Status = cfg[tank_id]["Alert_Pump Status"]
        # print(f"Alert_Liquid_Low:{Alert_Liquid_Low} Alert_Liquid_High:{Alert_Liquid_High}")
        try:
            c = ModbusClient(host=ipaddress, port=port, auto_open=True, auto_close=True,timeout=0.2)


            secondary_flow_rate_registers = c.read_holding_registers(secondary_flow_rate,1)[0]*0.1
            secondary_treturn_registers = c.read_holding_registers(secondary_treturn,1)[0]*0.1
            secondary_tsupply_registers = c.read_holding_registers(secondary_tsupply,1)[0]*0.1
            primary_tinlet_registers = c.read_holding_registers(primary_tinlet,1)[0]*0.1
            primary_pinlet_registers = c.read_holding_registers(primary_pinlet,1)[0]*0.1
            ta_registers = c.read_holding_registers(ta,1)[0]*0.1
            r_humidity_registers = c.read_holding_registers(r_humidity,1)[0]*0.1
            dew_point_registers = c.read_holding_registers(dew_point,1)[0]*0.1
            remove_heat_registers = c.read_holding_registers(remove_heat,1)[0]*0.1
            pump_output_registers = c.read_holding_registers(pump_output,1)[0]*0.1
            cooling_registers = c.read_holding_registers(cooling,1)[0]*0.1            

            secondary_flow_rate_registers = round(secondary_flow_rate_registers,1)
            secondary_treturn_registers = round(secondary_treturn_registers,1)
            secondary_tsupply_registers = round(secondary_tsupply_registers,1)
            primary_tinlet_registers = round(primary_tinlet_registers,1)
            primary_pinlet_registers = round(primary_pinlet_registers,1)
            ta_registers = round(ta_registers,1)
            r_humidity_registers = round(r_humidity_registers,1)
            dew_point_registers = round(dew_point_registers,1)
            remove_heat_registers = round(remove_heat_registers,1)
            pump_output_registers = round(pump_output_registers,1)
            cooling_registers = round(cooling_registers,1)
            
            # print("Sec.F.R.%.1f"%secondary_flow_rate_registers)
            # print("Sec.Treturn%.1f"%secondary_treturn_registers)
            # print("Sec.Tsupply%.1f"%secondary_tsupply_registers)
            # print("Pri.Tinlet%.1f"%primary_tinlet_registers)
            # print("Pri.Pinlet%.1f"%primary_pinlet_registers)
            # print("Tambient%.1f"%ta_registers)
            # print("R.Humidity%.1f"%r_humidity_registers)
            # print("Dew Point%.1f"%dew_point_registers)
            # print("Remove Heat%.1f"%remove_heat_registers)
            # print("Pump%.1f"%pump_output_registers)
            # print("Cooling%.1f"%cooling_registers)
            
            Alert_Secondary_Tsupply = c.read_discrete_inputs(Alert_Secondary_Tsupply,1)[0]
            Alert_Primary_Tinlet = c.read_discrete_inputs(Alert_Primary_Tinlet,1)[0]
            Alert_Primary_Pinlet = c.read_discrete_inputs(Alert_Primary_Pinlet,1)[0]
            Alert_Leakage = c.read_discrete_inputs(Alert_Leakage,1)[0]
            Alert_Fan_Status = c.read_discrete_inputs(Alert_Fan_Status,1)[0]
            Alert_Liquid_High = c.read_discrete_inputs(Alert_Liquid_High,1)[0]
            Alert_Liquid_Low = c.read_discrete_inputs(Alert_Liquid_Low,1)[0]
            Alert_Pump_Status = c.read_discrete_inputs(Alert_Pump_Status,1)[0]

            Liquid_Level = ""

            if Alert_Liquid_Low == 1:
                Liquid_Level = "Low"
            elif Alert_Liquid_Low == 0 and Alert_Liquid_High == 0:
                Liquid_Level = "Working"
            elif Alert_Liquid_Low == 0 and Alert_Liquid_High == 1:
                Liquid_Level = "Full"

            if Alert_Leakage == 0:
                Alert_Leakage = "Normal"
            elif Alert_Leakage == 1:
                Alert_Leakage = "Alert"
            else:
                pass

            if Alert_Pump_Status == 0:
                Alert_Pump_Status = "Normal"
            elif Alert_Pump_Status == 1:
                Alert_Pump_Status = "Alert"
            else:
                pass
            
            if Alert_Fan_Status == 0:
                Alert_Fan_Status = "Normal"
            elif Alert_Fan_Status == 1:
                Alert_Fan_Status = "Error"
            else:
                pass

            result = [
                name,secondary_flow_rate_registers,secondary_tsupply_registers,secondary_treturn_registers,remove_heat_registers,
                primary_tinlet_registers,primary_pinlet_registers,ta_registers,r_humidity_registers,dew_point_registers,
                pump_output_registers,cooling_registers,Liquid_Level,Alert_Leakage,Alert_Pump_Status,Alert_Fan_Status
                ]
            print("----------")
            # print(f"Alert_Liquid_Low:{Alert_Liquid_Low} Alert_Liquid_High:{Alert_Liquid_High}")
            # print("Liquid Level = Liquid_Low:%d,Luquid_High:%d"%(Alert_Liquid_Low,Alert_Liquid_High))
            # print("Liquild_High:%d"%Alert_Liquid_High)
            # print("Liquid_Low:%d"%Alert_Liquid_Low)

            # print("Alert_Leakage:%d"%Alert_Leakage)
            # print("Pump Status:%d"%Alert_Pump_Status)
            # print("System Fan:%d"%Alert_Fan_Status)
            
            print(result)


        except (TimeoutError, AttributeError,TypeError) as e:
            print(f"Error:{name},ip:{ipaddress}, {str(e)}")

        
        

