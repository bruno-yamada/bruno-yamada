# Kubectl

View resource requested/limit by deployment container:
```
kubectl get deploy -o json| jq -r ".items[].spec.template.spec.containers[] | {
container: .name,
cpu_limits: .resources.limits.cpu,
cpu_requests: .resources.requests.cpu,
mem_limits: .resources.limits.memory,
mem_requests: .resources.requests.memory,
}"
```
