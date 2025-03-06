# Patroni

```sh
sudo apt install postgresql-16 postgresql-16-client
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

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```sh
python3 -m venv .venv
source .venv/bin/activate
patroni postgres0.yml
```

```sh
python3 -m venv .venv
source .venv/bin/activate
patroni postgres1.yml
```
