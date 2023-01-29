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

2022-11-24 to 2022-12-01:

```
Light:  9403 (69.7%)
Dark:   4079 (30.3%)
Total: 13482 (100.0%)
```

2022-12-02 to 2022-12-08:

```
Light: 10819 (69.3%)
Dark:   4798 (30.7%)
Total: 15617 (100.0%)
```

2022-12-09 to 2022-12-15:

```
Light:  9897 (68.4%)
Dark:   4580 (31.6%)
Total: 14477 (100.0%)
```

2022-12-16 to 2022-12-22:

```
Light:  9031 (71.0%)
Dark:   3690 (29.0%)
Total: 12721 (100.0%)
```

2022-12-23 to 2022-12-29:

```
Light:  9153 (70.9%)
Dark:   3748 (29.1%)
Total: 12901 (100.0%)
```

2022-12-30 to 2023-01-05:

```
Light:  10725 (71.3%)
Dark:    4312 (28.7%)
Total:  15037 (100.0%)
```

2023-01-06 to 2023-01-12:

```
Light: 12577 (69.5%)
Dark:   5519 (30.5%)
Total: 18096 (100.0%)
```

2023-01-13 to 2023-01-19:

```
Light: 13628 (69.1%)
Dark:   6106 (30.1%)
Total: 19734 (100.0%)
```

2013-01-20 to 2023-01-26:

```
Light: 15031
Dark: 6725
```

[^1]: It's not a debate, since dark mode is clearly superior.
