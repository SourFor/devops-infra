# Prometheus & Grafana & Alertmanager

## Deploy with docker compose

```
docker compose up -d
docker ps -a
```
Stop and remove the containers. Use `-v` to remove the volumes if looking to erase all data.
```
$ docker compose down -v
```


## Run listener

'''
sudo nc -lk -p 777
'''

## Run script

'''
python3 alert-machinegun.py -c config.yml
'''

## Jenkins

