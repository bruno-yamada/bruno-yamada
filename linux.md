- ls
- du
- tail
- date
- cal
- find
- cat
- head

## bc
basic calculator 

```sh
echo "12+5" | bc # prints 17

bc -l # enters interactive mode
> a=3
> a*3 # prints 9
> quit # to quit
```

## cut
Split string, output slices from array
```sh
echo https://google.com/q?=teste | cut -d'/' -f 1-3 # outputs https://google.com
```
