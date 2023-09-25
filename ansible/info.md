--vault-password-file


ansible-playbook -i inventories/dev -t prepare -l localhost --vault-password-file vault.pass --become-pass-file become.pass playbooks/elk/elk.yml 

