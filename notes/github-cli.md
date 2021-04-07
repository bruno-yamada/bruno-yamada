
# List open issues
Across many services:
```
gh api -X GET search/issues -f q='user:bruno-yamada is:open' | jq -r .items[].title
```
