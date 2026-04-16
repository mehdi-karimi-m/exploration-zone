from pathlib import Path
from pprint import pprint
import json
from datetime import datetime


print(str(datetime.now()))

sample_data = [
    {"FirstName":  "Mehdi", "LastName": "Karimi", "Age": 43, "InsertDate": str(datetime.now())},
    {"FirstName":  "Mina", "LastName": "Taheri", "Age": 37, "InsertDate": str(datetime.now())},
    {"FirstName":  "Reza", "LastName": "Karimi", "Age": 74, "InsertDate": str(datetime.now())}
]

json_data = json.dumps(sample_data)

json_file_path = Path("data.json")
if json_file_path.exists():
    json_file_path.unlink()

json_file_path.write_text(json_data)


json_text = json_file_path.read_text()
data = json.loads(json_text)
pprint(data)
