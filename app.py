from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Nandini Rathod"  # 👈 Replace with your real full name if needed
    username = os.getenv("USER") or os.getenv("USERNAME")
    
    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")

    # Get top command output
    top_output = subprocess.getoutput("top -n 1 -b")

    return f"<pre>Name: {name}\nUser: {username}\nServer Time (IST): {server_time}\n\n{top_output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
