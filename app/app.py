import psutil
import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # 1. Calculate the numbers
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    hostname = socket.gethostname()
    
    # 2. Send them to the HTML (This was the missing link!)
    return render_template("index.html", 
                         cpu_metric=cpu_metric, 
                         mem_metric=mem_metric, 
                         hostname=hostname)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)