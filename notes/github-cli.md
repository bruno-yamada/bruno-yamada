# Cheatsheet on using gh-cli

## List open issues
Across many services:
```
gh api -X GET search/issues -f q='user:bruno-yamada is:open' | jq -r .items[].title
```

## List repositories from an org

```
gh api -X GET search/repositories -F q='org:<org> <some-string>' | jq -r '.items[].name'
```

