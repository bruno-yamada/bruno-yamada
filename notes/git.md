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

## Sign your commits (using ssh)
generate your key if you haven't already:
```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

```bash
# set sign format
git config --global gpg.format ssh

# set to always sign
git config --global commit.gpgsign true
git config --global tag.gpgsign true

# set your signing key
git config --global user.signingkey 'key::ssh-ed25519 AAAAC3(...) user@example.com'
```

On github, you can also add the key as a "signing" key in your `user settings`
