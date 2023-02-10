# Premise

A common debate[^1] is whether light or dark mode is better.
This is an attempt to document which is more popular on [qbreader](https://www.qbreader.org).

## Technical Details

If a user has a system preference, then qbreader uses that.
Otherwise, qbreader defaults to the previously selected mode.
If no mode has been selected, then qbreader defaults to light mode.

The following SQL queries are used to determine the number of requests for light and dark mode.

### Light/Dark Mode

```SQL
SELECT message
FROM $table

WHERE
    dt BETWEEN toDateTime64($from, 3)
    AND toDateTime64($to, 3)
    AND message LIKE 'at=info method=GET path="/bootstrap/light.css"%'
```

For dark mode, swap out `light.css` for `dark.css`.

## Results

| Dates                    | Light         | Dark         | Total          |
| ------------------------ | ------------- | ------------ | -------------- |
| 2022-11-24 to 2022-12-01 | 9403 (69.7%)  | 4079 (30.3%) | 13482 (100.0%) |
| 2022-12-02 to 2022-12-08 | 10819 (69.3%) | 4798 (30.7%) | 15617 (100.0%) |
| 2022-12-09 to 2022-12-15 | 9897 (68.4%)  | 4580 (31.6%) | 14477 (100.0%) |
| 2022-12-16 to 2022-12-22 | 9031 (71.0%)  | 3690 (29.0%) | 12721 (100.0%) |
| 2022-12-23 to 2022-12-29 | 9153 (70.9%)  | 3748 (29.1%) | 12901 (100.0%) |
| 2022-12-30 to 2023-01-05 | 10725 (71.3%) | 4312 (28.7%) | 15037 (100.0%) |
| 2023-01-06 to 2023-01-12 | 12577 (69.5%) | 5519 (30.5%) | 18096 (100.0%) |
| 2023-01-13 to 2023-01-19 | 13628 (69.1%) | 6106 (30.1%) | 19734 (100.0%) |
| 2013-01-20 to 2023-01-26 | 15031 (69.1%) | 6725 (30.9%) | 21756 (100.0%) |
| 2023-01-27 to 2023-02-02 | 16909 (68.7%) | 7720 (31.3%) | 24629 (100.0%) |
| 2023-02-03 to 2023-02-09 | 16645 (69.3%) | 7380 (30.7%) | 24025 (100.0%) |

[^1]: It's not a debate, since dark mode is clearly superior.
