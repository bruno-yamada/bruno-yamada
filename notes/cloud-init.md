# Cloud Init

TODO description



# Add a new user with ssh access
```
#cloud-config
cloud_final_modules:
- [users-groups,always]
users:
  - name: username
    groups: [ wheel ]
    sudo: [ "ALL=(ALL) NOPASSWD:ALL" ]
    shell: /bin/bash
    ssh-authorized-keys:
    - ssh-rsa AB3nzExample
```

