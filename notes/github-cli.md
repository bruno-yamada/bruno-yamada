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

## Watching (notifications)

List watched repos
```
gh api -X GET -f per_page=100 user/subscriptions | jq -r '.[].full_name'
```

List all
```
FINISHED=
REPOS=
PAGE=1
while [ -z "$FINISHED" ]; do
  REQ_REPOS=$(gh api -X GET -f per_page=100 -f page=$PAGE user/subscriptions | jq -r '.[].full_name')
  if [ -z "$REQ_REPOS" ]; then
    FINISHED="true"
  else
    PAGE=$((PAGE+1))
    REPOS="$REPOS $REQ_REPOS"
  fi
done

echo $REPOS | tr " " "\n"
```

Remove a subscription

_(will go back to default: only participating and @mentions will work)_
```
gh api -X DELETE repos/<owner>/<repository_name>/subscription
```

