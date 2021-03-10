# About vim


## BANG, using :.! and stuff
> ref: https://rwx.gg/tools/editors/vi/how/magic/

Type `!` twice, than type the command you want, the output will be piped to vim
```
:.!ls -la 
```

Optionally, type a line in vim, and have it be interpreted:
```
# type:
ls -al
# 2x ! and enter the interpreter
:.!bash
# the output will be send to vim
```

With the above you can also type perl, python, and use them to interpret the code:
```
[print(i) for i in range(1, 21)]
```

## Delete lines based on regex
```
:g/my-exp/d
```

## Flags

get flag help(really useful)
```
:h hlsearch
```

ls -la
