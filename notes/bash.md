
while read i; do echo "$i"; done < ./file_wget_med

git branch --merged | grep -v \* | xargs git branch -D
