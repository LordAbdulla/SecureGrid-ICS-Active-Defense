import time
import threading
import random
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.client import ModbusTcpClient

def run_plc_server():
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [0]*100),
        co=ModbusSequentialDataBlock(0, [0]*100),
        hr=ModbusSequentialDataBlock(0, [0]*100), # Holding Registers
        ir=ModbusSequentialDataBlock(0, [0]*100)) 
    
    context = ModbusServerContext(slaves=store, single=True)
    
    print("[+] PLC (Turbine Sensor) Started on localhost:5020\n To stop Ctrl+c")
    StartTcpServer(context=context, address=("localhost", 5020))

def run_hmi_client():
    time.sleep(2) 
    client = ModbusTcpClient('localhost', port=5020)
    client.connect()
    
    print("[+] HMI (Control Center) Connected..\n Reading Data...")

    while True:
        normal_temp = random.randint(60, 65)
        client.write_register(0, normal_temp, slave=1)

        rr = client.read_holding_registers(0, 1, slave=1)
        if not rr.isError():
            print(f"[Normal] Turbine Temp: {rr.registers[0]}°C")
        
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=run_plc_server)
    t.daemon = True
    t.start()

    run_hmi_client()
