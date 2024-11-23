## INSTALL ELASTICSEARCH

```
ansible-playbook -i inventories/local-test -t prepare,configure_cluster -l local --vault-pass-file vault.pass  playbooks/elk/elk.yml 
```
## INSTALL KIBANA

```
ansible-playbook -i inventories/local-test -t kibana -l local --vault-pass-file vault.pass playbooks/elk/elk.yml 

```

## INSTALL FILEBEAT

```
ansible-playbook -i inventories/local-test -l local --vault-pass-file vault.pass  playbooks/elk/filebeat.yml 
```

## INSTALL ALERT-MACHINEGUN

```
ansible-playbook -i inventories/local-test -l local --vault-pass-file vault.pass  playbooks/prometheus/alert_machinegun.yml 
```

## INSTALL JENKINS

```
ansible-playbook -i inventories/local-test -l local --vault-pass-file vault.pass  playbooks/jenkins/jenkins.yml 
```
