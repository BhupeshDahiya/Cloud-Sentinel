import socket
import platform
import psutil
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Gather System Info
    system_info = {
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "os_platform": platform.system(),
        "os_release": platform.release(),
        "cpu_count": psutil.cpu_count(),
        "memory_total": f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB",
        "python_version": platform.python_version()
    }
    
    return render_template('index.html', info=system_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)