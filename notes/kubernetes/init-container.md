# Init Containers

Init containers are a useful resource for when you need to do some task before
your main container is executed

Common use cases:
- Run Database migrations
- Send notifications about a container being started
- Make some validation checks such as checking the health of other apis the container depends upon
- Fetch secrets from somewhere so that they can be made available for other containers

Considerations:
- An init container, by default, does not share volumes with other containers, so you are safe having secrets in them without the risks of the secrets being present in the main container

## Examples

Fetching some artifact and making it available for the other containers

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-container-example
  labels:
    app: myapp
spec:
  containers:
  - name: main-container
    image: alpine
    command: [ 'sh', '-c' ]
    args:
      - echo "The app is running!";
        ls -la /tmp/artifacts
        sleep 3600;
    volumeMounts:
    - name: tmp
      mountPath: /tmp/artifacts
  initContainers:
  - name: init-container
    image: alpine
    command: [ 'sh', '-c' ]
    args:
      - apk add curl;
        curl https://some-url/some-fictional-file.tar --output /tmp/artifacts/file.tar;
    volumeMounts:
    - name: tmp
      mountPath: /tmp/artifacts
  volumes:
  - name: tmp
    emptyDir: {}
```
