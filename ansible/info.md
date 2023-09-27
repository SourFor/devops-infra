## INSTALL ELASTICSEARCH

```
ansible-playbook -i inventories/local-test -t prepare,configure_cluster -l local --vault-pass-file vault.pass  playbooks/elk/elk.yml 
```
## INSTALL KIBANA

```
ansible-playbook -i inventories/local-test -t enroll_kibana -l local --vault-pass-file vault.pass playbooks/elk/elk.yml 
# TO DO 
sudo podman exec kibana bin/kibana-verification-code
```

## INSTALL FILEBEAT

```
ansible-playbook -i inventories/local-test -l local --vault-pass-file vault.pass  playbooks/elk/filebeat.yml 
```
