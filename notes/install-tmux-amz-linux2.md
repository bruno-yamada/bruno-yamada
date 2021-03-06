# Install latest TMUX on Amazon Linux 2
Dependencies:
```
sudo yum install automake libevent-devel ncurses-devel
sudo yum group install "Development Tools"
```

Clone and install:
```
git clone --depth 1 https://github.com/tmux/tmux.git ~/.tmux-tmp
cd ~/.tmux-tmp
sh autogen.sh
./configure && make
sudo cp tmux /usr/local/bin/
```

Optionally clear `~/.tmux-tmp`
```
rm -rf ~/.tmux-tmp
```

