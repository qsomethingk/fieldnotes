---
type: meta
---

# Reading Queue

```dataview
TABLE author, host, tags, created, published
FROM "notes"
WHERE status = "foreign"
SORT created DESC
```
