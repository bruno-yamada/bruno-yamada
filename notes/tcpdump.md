# Check packages
tcpdump -eee -ttt -vvv -n host 10.125.110.10

# Check on port
tcpdump -e -ttt -vvv port 22

# Check on range
tcpdump -e -ttt -vvv net 10.120.0.0/16

# filter by packet content
tcpdump -vvAls0|grep 'IP'

tcpdump -s 0 -v -n -l | egrep -i "/api/history"

tcpdump -s 0 -v -n -l | egrep -i "X-Forwarded-For"
tcpdump -s 0 -v -n -l | egrep -i "X-Forwarded-Proto"

# dump udp
tcpdump -i eth0 udp


# netcat
> listen on port 80
nc -lb 80