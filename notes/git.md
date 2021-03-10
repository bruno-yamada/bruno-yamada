# Undo shallow clones
```
# shallow clones wont have all branches, need to change it manually
git remote set-branches origin '*'

# will effectively fetch all commits
git fetch --unshallow
```
