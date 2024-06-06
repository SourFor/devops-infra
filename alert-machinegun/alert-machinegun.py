import argparse
import requests
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("secret_path", help="Path to the file with login and password")
args = parser.parse_args()

with open(args.secret_path, "r") as file:
 data = yaml.safe_load(file)

login = data["login"]
password = data["password"]

headers = {
 "Content-Type": "application/json"
}

data = {
 "labels": {
 "alertname": "Scheduled alert"
 },
 "annotations": {
 "info": "This alert was sent by the verification tool"
 },
 "startsAt": "2024-06-03T20:07:50",
 "endsAt": "2024-06-03T20:12:50",
 "generatorURL": "localhost:80"
}

response = requests.post("www.example.org", data=json.dumps(data), headers=headers, auth=(login, password))

print(response.status_code)


from datetime import datetime, timezone                                
local_time = datetime.now(timezone.utc).astimezone()
local_time.isoformat()