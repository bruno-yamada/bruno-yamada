# Curl

## redirect output to the file
curl http://url/file > file

## write to file instead of stdout
curl -o file http://url/file
curl --output file http://url/file

## write output to a file named as the remote file
curl -o file http://url/file
curl --output file http://url/file

## execute remote script
bash <(curl -s http://url/myscript.sh)

## basic auth
curl -u username:password http://example.com

## Allow insecure connection
curl -k https://example.com

## Curl with POST
curl -X POST -H "Content-Type: application/json" -d @FILENAME http://example.com
