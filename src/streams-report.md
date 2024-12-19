---
title: Streams Report
header: |
  <div class="banner">
    <p> Let's see if this works! </p>
  </div>
sql:
  streams: data/streams.csv
---

```sql
SELECT * FROM streams WHERE week_number = 50 LIMIT 10;
```