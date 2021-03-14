# elasticsearch cheatsheet

## list all indices
```
curl -u user:pass $HOST:9200/_cat/indices?v
``` 

# clsuter health
curl localhost:9200/_cluster/health

# list indices
curl localhost:9200/_cat/indices

# Query
curl -XPOST -d '{"query": {"match": {"source":"api-*"}}, "sort": [{"timestamp": "desc"}]}'  localhost:9200/graylog_306/_search

curl -XPOST -d '{"query": {"match": {"streams":"5b031f8e8eefc00503815691"}}, "sort": [{"timestamp": "desc"}]}'  localhost:9200/graylog_306/_search
