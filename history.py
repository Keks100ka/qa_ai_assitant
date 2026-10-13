import json
import os
from datetime import datetime
from config import HISTORY_FILE

def _load_history():

    if not os.path.exists(HISTORY_FILE):
        return []
    
    with open(HISTORY_FILE, "r", encoding="utf-8") as f: #f = open(HISTORY_FILE, "r", encoding="utf-8") finally: f.close()
        return json.load(f)


def _save_history(records):

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        return json.dump(records, f)


def add_record(command, input_text, output_text):

    history = _load_history

    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "command": command,
        "input": input_text,
        "output": output_text
    }

    history.extend(record)
    _save_history(history)



