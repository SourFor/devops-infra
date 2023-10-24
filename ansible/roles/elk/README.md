Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

```
# create certs
podman run --name elastis docker.io/elastic/elasticsearch:8.9.2
podman exec -ti elastis bin/elasticsearch-certutil ca -s --out config/certs/elk-cluster-ca.p12 --pass {{ elasticsearch_keystore_password }}
podman exec -ti elastis bin/elasticsearch-certutil cert -s --ca config/certs/elk-cluster-ca.p12 --out config/certs/elk-transport.p12 --ca-pass {{ elasticsearch_keystore_password }} --pass {{ elasticsearch_keystore_key_password }}

# copy from container
cd [role_dir]/files/elasticsearch/configs/certs
podman cp elastic:/usr/share/elasticsearch/config/certs/elk-transport.p12 .
podman cp elastic:/usr/share/elasticsearch/config/certs/elk-cluster-ca.p12 .

# check
keytool -v -list -storetype pkcs12 -keystore elk-transport.p12 
keytool -v -list -storetype pkcs12 -keystore elk-cluster-ca.p12
```

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

ansible-playbook -i inventories/local-test -t prepare,configure_cluster -l local_cluster --vault-pass-file vault.pass  playbooks/elk/elk.yml

ansible-playbook -i inventories/local-test -t kibana -l local_cluster --vault-pass-file vault.pass  playbooks/elk/elk.yml

ansible-playbook -i inventories/local-test -l local_cluster -t filebeat --vault-pass-file vault.pass  playbooks/elk/elk.yml

ansible-playbook -i inventories/local-test -l local_cluster -t flush -e "elastic_flush=true" --vault-pass-file vault.pass  playbooks/elk/elk.yml

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
