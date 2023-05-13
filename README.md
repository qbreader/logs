# qbreader/logs

A repository to manage the logs produced by [qbreader](https://www.qbreader.org).
Produces summary data of the following per week:

1. The most popular sets
2. The most active and number of distinct singleplayer users, by IP address
3. The most popular (sub)categories and difficulties, across both singleplayer and multiplayer
4. The most popular and the number of distinct queries to the database
5. The most active and # of distinct multiplayer rooms, users, and usernames

## Privacy

Any files containing IP address should be hidden from this public repository by placing them in a `raw.log` file or by appropriately modifying the `.gitignore` file.

## Obtaining Logs

[qbreader](https://www.qbreader.org/) is hosted on [Heroku](https://www.heroku.com/) with [Logtail](https://betterstack.com/logtail) integration.
Specific types of logs are queried from Logtail using Grafana with the following SQL queries (see section below).
The values are saved in `raw.log` (in the appropriate folder) and processed using the `summarize.py` script.

### Singleplayer Packet Requests

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND message LIKE 'at=info method=GET path="/api/packet%'
```

### Database Random Questions

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND (
        message LIKE 'at=info method=GET path="/api/random-tossup%'
        OR message LIKE 'at=info method=GET path="/api/random-bonus%'
    )
```

### Database Queries

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND message LIKE 'at=info method=GET path="/api/query%'
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
