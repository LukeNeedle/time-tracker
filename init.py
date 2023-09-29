from flask import Flask, request
import sqlite3
import json
import threading
import datetime

app = Flask(__name__)
app.secret_key = 'eryUJT3RFE891273Rfrgsgh%^$*(YT9Q3H4T0Q987ERGY9U8&t*&tyg*ogt^g)()'

def timer():
    while not stop:
        if (f"{datetime.datetime.now().strftime('%M')}" in ["0","15","30","45"]):
            pass


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
    print(data)
    cur.execute(f"""d""")
    conn.close()
    return "Submitted"

def send_ui():
    import main

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')