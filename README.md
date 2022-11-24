# qbreader/logs

A repository to manage the logs produced by [qbreader](https://www.qbreader.org).
Produces summary data of the most popular sets and most active users (by IP) for the given raw logs.

## Privacy

Any files containing IP address should be hidden from this public repository by placing them in either old/, api-packet.txt, summary-ip.txt, or by appropriately modifying the .gitignore file.

## Obtaining Logs

QB Reader is hosted on [Heroku](https://www.heroku.com/) with [Logtail](https://betterstack.com/logtail) integration.
We are interested in how often certain sets are requested (not including multiplayer).
Heroku logs of requests to the `/api/packet-tossups` or `/api/packet-bonuses` endpoints are queried from Logtail using Grafana with the following SQL queries:

### Singleplayer Packet Requests

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND message LIKE 'at=info method=GET path="/api/packet%'
```

The values are saved in `api-packet.txt` and processed using the `summarize-raw.py` script.

### Singleplayer Random Questions

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND proc_id = 'web.1'
    AND message LIKE 'DATABASE RANDOM QUESTIONS%'
```

### Database Queries

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND proc_id = 'web.1'
    AND message LIKE 'DATABASE QUERY%'
```

### Multiplayer Connections

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND proc_id = 'web.1'
    AND message LIKE 'Connection%'
```
