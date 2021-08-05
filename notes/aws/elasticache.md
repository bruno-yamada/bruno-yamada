# Elasticache

## Redis
Redis elasticache can be used with encryption in-transit enabled,
meaning it requires ssl, so when trying to connect using redis-cli you might
not be able to do it unless you configure a tunnel with something line stunnel

For testing purposes it might be easier to use python:
```
import redis
r = redis.Redis(host=host, ssl=True, password=password)
r.set('test-key', 'test-value')
r.get('test-key')
```

refs:
- [stunnel](https://www.stunnel.org/)
Some resources:
- https://help.compose.com/docs/redis-and-redis-cli#section-using-redis-cli-with-ssltls
- https://kevinhakanson.com/2018-06-27-making-a-secure-connection-to-elasticache-redis
