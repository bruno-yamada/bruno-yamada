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

## Interactice rebase
TODO ammend commit in history:
- https://stackoverflow.com/questions/1186535/how-to-modify-a-specified-commit

## Diff
Diff between current and current-1
```
git diff HEAD~..HEAD --name-only
```
