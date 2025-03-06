# Patroni

### terminal №1

```sh
sudo apt install python3 postgresql-16 postgresql-16-client
sudo systemctl stop postgresql
```

create data dirs

```sh
cd test_area/patroni
mkdir -p data/etcd
mkdir -p data/postgres/postgresql0
mkdir data/postgres/postgresql1
chmod 700 data/postgres/postgresql0 data/postgres/postgresql1
```

```sh
ETCD_VER=v3.5.18
GOOGLE_URL=https://storage.googleapis.com/etcd
GITHUB_URL=https://github.com/etcd-io/etcd/releases/download
DOWNLOAD_URL=${GOOGLE_URL}
curl -L ${DOWNLOAD_URL}/${ETCD_VER}/etcd-${ETCD_VER}-linux-amd64.tar.gz -o /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz
tar xzvf /tmp/etcd-${ETCD_VER}-linux-amd64.tar.gz -C /usr/local/bin/ --strip-components=1
sudo tar xzvf  -C /usr/local/bin/ --strip-components=1
/usr/local/bin/etcd --config-file etcd.conf.yml.sample
```

### terminal №2
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
patroni postgres0.yml
```

### terminal №3

```sh
source .venv/bin/activate
patroni postgres1.yml
```

## haproxy

### terminal №4

```sh
sudo apt install haproxy
sudo systemctl stop haproxy
```

```sh
/usr/sbin/haproxy -f haproxy.cfg -p /run/haproxy-test.pid -S /run/haproxy-test.sock
```

## test

### terminal №5

```sh
psql -U postgres -h 127.0.0.1 -p 5000
\conninfo
SHOW PORT;
```

stop leader postgresql or patrony ( press `ctrl+c` in terminal №1 or terminal №2 ) and check port number in the psql terminal again

```sh
SHOW PORT;
```

## etcd help

```sh
etcdctl --endpoints=127.0.0.1:3379  member list
```

## next steps

- create systemd services
