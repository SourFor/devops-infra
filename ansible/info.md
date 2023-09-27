## INSTALL ELASTICSEARCH
```
ansible-playbook -i inventories/dev -t prepare,configure_cluster -l localhost --vault-pass-file vault.pass  playbooks/elk/elk.yml 
```
## INSTALL KIBANA
```
ansible-playbook -i inventories/dev -t enroll_kibana -l localhost --vault-pass-file vault.pass  playbooks/elk/elk.yml 
```
