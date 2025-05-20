from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(0.2)
    return "Server publik dari Railway!"

    app.run(host='0.0.0.0', port=5000)
