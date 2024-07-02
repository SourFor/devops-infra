import argparse
import json
import requests
import yaml
from datetime import datetime, timezone 

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help="Path to the file with login and password")
args = parser.parse_args()

with open(args.config, "r") as file:
 data = yaml.safe_load(file)

login = data["login"]
password = data["password"]
server = data["server"] + '/api/v2/alerts'

local_time = datetime.now(timezone.utc).astimezone()
local_time.isoformat()

headers = {
 "Content-Type": "application/json"
}

alert = {
    "labels": {
        "alertname": "Scheduled alert"
    },
    "annotations": {
        "info": "This alert was sent by the verification tool"
    },
    "startsAt": local_time.isoformat(),
    "generatorURL": "localhost:80"
}
data = []
data.append(alert)
print(json.dumps(data))
response = requests.post(server, data=json.dumps(data), headers=headers, auth=(login, password))
print(response.status_code)