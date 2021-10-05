# Bash

This does not contain all bash commands, for that instead refer to `man bash`o

This is just some of my findings when digging through the manual

## Moving around in bash

> All of these are available in the "man bash" docs

`Ctrl+A`: Goes to the beginning of the command
`Ctrl+E`: Goes to the beginning of the command
`Ctrl+K`: "kills" (cut) from the cursor onwards
`Ctrl+Y`: "yank"(paste) back stuff you removed with Ctrl+K
`Ctrl+u`: discard/clear current likne
`Ctrl+x Backspace`: cut from cursor backwards
`Ctrl+w`: cut word back, one at a time

!!        # repeats the last command
!<n>      # refers to command line 'n'
!<string> # refers to command starting with 'string'

whereis bash  # locates the binary, source and manual-page for a command
which bash    # finds out which program is executed as 'bash' (default: /bin/bash, can change across environments)

cd -  # changes to previous working directory
