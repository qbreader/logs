# Premise

A common debate[^1] is whether light or dark mode is better.
This is an attempt to document which is more popular on [qbreader](https://www.qbreader.org).

## Technical Details

If a user has a system preference, then qbreader uses that.
Otherwise, qbreader defaults to the previously selected mode.
If no mode has been selected, then qbreader defaults to dark mode[^2].

The following SQL queries are used to determine the number of requests for light and dark mode.

### Light/Dark Mode

To find the **total** number of visits (not just dark mode), use the following SQL query:

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND message LIKE 'at=info method=GET path="/bootstrap/dark.css"%'
```

Explanation: when a user visits qbreader, the server logs a request for `dark.css`.
If their preference is light mode, then the client makes an _additional_ request for `light.css`.

For light mode, swap out `dark.css` for `light.css`.

## Results

| Dates                        | Light         | Dark         | Total          |
| ---------------------------- | ------------- | ------------ | -------------- |
| 2022-11-24 to 2022-12-01     | 5324 (56.6%)  | 4079 (43.4%) | 9403 (100.0%)  |
| 2022-12-02 to 2022-12-08     | 6021 (55.6%)  | 4798 (44.4%) | 10819 (100.0%) |
| 2022-12-09 to 2022-12-15     | 5317 (53.7%)  | 4580 (46.3%) | 9897 (100.0%)  |
| 2022-12-16 to 2022-12-22     | 5341 (59.1%)  | 3690 (40.9%) | 9031 (100.0%)  |
| 2022-12-23 to 2022-12-29     | 5405 (59.0%)  | 3748 (41.0%) | 9153 (100.0%)  |
| 2022-12-30 to 2023-01-05     | 6413 (59.7%)  | 4312 (40.3%) | 10725 (100.0%) |
| 2023-01-06 to 2023-01-12     | 7058 (56.1%)  | 5519 (43.9%) | 12577 (100.0%) |
| 2023-01-13 to 2023-01-19     | 7522 (55.1%)  | 6106 (44.9%) | 13628 (100.0%) |
| 2013-01-20 to 2023-01-26     | 8306 (55.2%)  | 6725 (44.8%) | 15031 (100.0%) |
| 2023-01-27 to 2023-02-02     | 9189 (54.3%)  | 7720 (45.7%) | 16909 (100.0%) |
| 2023-02-03 to 2023-02-09     | 9265 (55.6%)  | 7380 (44.4%) | 16645 (100.0%) |
| 2023-02-14 to 2023-02-16[^3] | 5370 (58.6%)  | 3790 (41.4%) | 9160 (100.0%)  |
| 2023-02-17 to 2023-02-23[^4] | 10222 (54.9%) | 8391 (45.1%) | 18613 (100.0%) |
| 2023-02-24 to 2023-03-02     | 10721 (55.1%) | 8745 (44.9%) | 19466 (100.0%) |
| 2023-03-03 to 2023-03-09     | 11154 (53.7%) | 8745 (46.3%) | 20760 (100.0%) |
| 2023-03-10 to 2023-03-16     | 10554 (54.9%) | 8745 (45.1%) | 19223 (100.0%) |
| 2023-03-17 to 2023-03-23     | 11649 (54.1%) | 9899 (45.9%) | 21548 (100.0%) |
| 2023-03-24 to 2023-03-30     | 11313 (55.4%) | 9116 (44.5%) | 20429 (100.0%) |

[^1]: It's not a debate, since dark mode is clearly superior.
[^2]: I attempted to change the default theme [from light mode to dark mode](https://github.com/qbreader/website/commit/d267dcebe84a6e2309b4e1c89d6e03156efcc661) on 2023-02-10, but I did not actually change anything. I successfully changed it [here](https://github.com/qbreader/website/commit/12f2e6842d48cae53fa2993a06b9212b06345f46).
[^3]: Over the course of 2023-02-10 to 2023-02-13, the server was DDoS'd, so Grafana was unable to store all the logs and I had to delete and restart log collection.
[^4]: The first week that the default theme was dark mode.
