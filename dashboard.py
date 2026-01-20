from flask import Flask, render_template_string
import random

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>SecureGrid Dashboard - Bahrain Power</title>
    <meta http-equiv="refresh" content="2"> <style>
        body { font-family: sans-serif; text-align: center; background-color: #1a1a1a; color: white; }
        .status-box { padding: 40px; border-radius: 10px; display: inline-block; margin-top: 50px; border: 2px solid white; }
        .safe { background-color: #2ecc71; }
        .danger { background-color: #e74c3c; animation: blink 1s infinite; }
        @keyframes blink { 50% { opacity: 0.5; } }
    </style>
</head>
<body>
    <h1>Bahrain Smart Grid Monitor</h1>
    <h2>Turbine #4 Status (Riffa Station)</h2>
    
    <div class="status-box {{ status_class }}">
        <h1 style="font-size: 80px; margin: 0;">{{ temp }}°C</h1>
        <h3>{{ message }}</h3>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    current_temp = random.choice([60, 62, 61, 63, 65, 60, 950]) 
    
    if current_temp > 100:
        return render_template_string(html_template, temp=current_temp, message="⚠️ ANOMALY DETECTED", status_class="danger")
    else:
        return render_template_string(html_template, temp=current_temp, message="System Normal", status_class="safe")

if __name__ == '__main__':
    print("Starting Dashboard on http://127.0.0.1:5001")
    app.run(port=5001)
