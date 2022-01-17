from ast import excepthandler
import datetime
import json
from pathlib import Path
import uuid

path_name = 'data.json'
path = Path(path_name)


def generate():
    id = uuid.uuid4()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = {date: id.hex}
    return result


def save_time_uuid(d):

    if path.exists():
        with open('data.json') as file:
            data = json.load(file)
        data.update(d)
        with open('data.json', 'w') as file:
            file.write(json.dumps(data))
    else:
        with open(path_name, 'w') as file:
            file.write(json.dumps(d))


def read_time_uuid_file():

    if path.exists():
        with open(path_name) as file:
            data = json.load(file)
        return data
    else:
        return {"message": "No data found, please visit /generate."}