import pandas as pd
from sklearn.ensemble import IsolationForest
from pymodbus.client import ModbusTcpClient
import time
import random
import sys

print("[*] Training AI Model on Normal Traffic Patterns...")
data = {'value': []}
for _ in range(2000): 
    data['value'].append(random.uniform(60.0, 65.0)) 

df_train = pd.DataFrame(data)
model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
model.fit(df_train[['value']]) 

print("[+] AI Model Trained. Connecting to Live Plant...")

client = ModbusTcpClient('localhost', port=5020)
client.connect()

print("\n--- 🛡️  SECUREGRID IPS ACTIVE (AUTO-RESPONSE ON) 🛡️  ---")

try:
    while True:
        rr = client.read_holding_registers(0, 1, slave=1)
        
        if not rr.isError():
            live_temp = rr.registers[0]
            
            prediction = model.predict(pd.DataFrame({'value': [live_temp]}))
            
            if live_temp > 100 or prediction[0] == -1:
                print(f"\n🚨 ALERT! Attack Detected: {live_temp}°C")
                
                print(f"⚔️  ENGAGING DEFENSE: Overwriting Malicious Value...")
                client.write_register(0, 60, slave=1) 
                
                print(f"✅ THREAT NEUTRALIZED: Turbine Reset to 60°C")
                time.sleep(1) 
                
            else:
                sys.stdout.write(f"\r✅ System Normal: {live_temp}°C   ")
                sys.stdout.flush()
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n[!] Monitoring Stopped.")
    client.close()
