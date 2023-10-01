from flask import Flask, request
import sqlite3
import json
import threading
import datetime
import main
import time

app = Flask(__name__)
app.secret_key = 'eryUJT3RFE891273Rfrgsgh%^$*(YT9Q3H4T0Q987ERGY9U8&t*&tyg*ogt^g)()'

def timer():
    main.window()
    while not stop:
        if (f"{datetime.datetime.now().strftime('%M')}" in ["00","15","30","45"]):
            main.window()
            time.sleep(70)

stop = False
t = threading.Thread(target=timer)
t.daemon = True
t.start()

@app.route('/', methods=['POST'])
def index():
    conn = sqlite3.connect("storage.db")
    cur = conn.cursor()
    data = json.loads(request.data)
    task = data["task"]
    timestamp = data["timestamp"]
    cur.execute(f"""INSERT INTO data(task, timestamp) VALUES ('{task}', '{timestamp}');""")
    conn.commit()
    conn.close()
    return "Submitted"

@app.route('/stop', methods=['POST', 'GET'])
def stopping():
    global stop
    stop = True
    return "stopped"

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')