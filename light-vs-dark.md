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

[^1]: It's not a debate, since dark mode is clearly superior.
