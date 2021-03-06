- ls
- du
- tail
- date
- cal
- find
- cat
- head

# User management
Create user:
```
N_USER=bruno
sudo useradd $N_USER --disabled-password

# for ubuntu
sudo usermod -aG sudo $N_USER

# for amazon linux
sudo usermod -aG wheel $N_USER
```



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

