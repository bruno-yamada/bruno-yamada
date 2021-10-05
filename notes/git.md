# Git

TODO: go through all `man git`

## Undo shallow clones
```
# shallow clones wont have all branches, need to change it manually
git remote set-branches origin '*'

# will effectively fetch all commits
git fetch --unshallow
```

## Undoing commit
undo last commit
```
git reset --soft HEAD~1
```
