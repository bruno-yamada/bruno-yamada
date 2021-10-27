# Homebrew

- `brew update` fetch latest version of homebrew and formulas
- `brew upgrade` upgrate outdated installations
- `brew upgrade <formula>` upgrate specific installation
- `brew pin <formula>` formula will be pinned and won't be upgraded through
  `upgrade` command
- `brew unpin <formula>` duh

## List all taps

```
brew tap-info --installed
```

## add tap from git
Install from github
```
brew tap my-user/my-tap
# will install from github.com/my-user/my-tap
```

or from private git, eg.
```bash
brew tap my-user/my-tap user@my-private-git.com/my-user/my-tap
```

## Remove a tap
```bash
brew untap my-user/my-tap 
```

## List installed brews
```
brew list
```

## Local tap

> TODO test if it works
From the tap directory
```bash
mkdir -p `brew --repo`/Library/Taps/local
ln -s $PWD `brew --repo`/Library/Taps/local/homebrew-my-tap
```

