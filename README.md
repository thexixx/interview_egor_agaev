You have dataset of the following structure:

```code
TOPIC<STRING>, TITLE<STRING>,  PAGES <ARRAY<STRUCT<PAGE<INT>, TEXT<STRING>>>>
```
```text
+--------+---------+--------------------------------------------------------------------------------------------------+
| TOPIC  | TITLE   | PAGES                                                                                            |
+--------+---------+--------------------------------------------------------------------------------------------------+
| Nature | Mammals | [{page: 1, text: "some text 1"}, {page: 2, text: "text 2"}]                                      |
| Nature | Oceans  | [{page: 1, text: "something 1"}, {page: 2, text: "some text 2"}, {page: 3, text: "some 3"}]      |
| Nature | Trees   | [{page: 1, text: "text"}]                                                                        |
| Auto   | Cars    | [{page: 1, text: "sometext"}]                                                                    |
| Auto   | Moto    | [{page: 1, text: "sometext1"}, {page: 2, text: "some text 2"}, {page: 3, text: "some text 3"}]   |
| Auto   | Trucks  | [{page: 1, text: "some text 1"}, {page: 2, text: "stext 2"}]                                     |
| Science| Physics | [{page: 1, text: "s1"}, {page: 2, text: "somxt2"}, {page: 3, text: "some text 3"}]               |
+--------+---------+--------------------------------------------------------------------------------------------------+
```

Write PySpark function "process_topic" which has above data as input and returns following dataframe:
```code
TOPIC<STRING>, TITLE<STRING>, PAGE<INT>, TEXT<STRING>, AVG_CHARS_PER_PAGE<LONG>
```
```text
+--------+---------+--------------------+--------------------+
| TOPIC  | TITLE   | PAGE | TEXT        | AVG_CHARS_PER_PAGE |
+--------+---------+--------------------+--------------------+
| Nature | Oceans  | 1    | something 1 | 9                  |
| Nature | Oceans  | 2    | some text 2 | 9                  |
| Nature | Oceans  | 3    | some 3      | 9                  |
| Nature | Mammals | 1    | some text 1 | 8                  |
| Nature | Mammals | 2    | text 2      | 8                  |
| Auto   | Moto    | 1    | sometext1   | 10                 |
| Auto   | Moto    | 2    | some text 2 | 10                 |
| Auto   | Moto    | 3    | some text 3 | 10                 |
| Auto   | Trucks  | 1    | some text 1 | 9                  |
| Auto   | Trucks  | 2    | stext 2     | 9                  |
| Science| Physics | 1    | s1          | 6                  |
| Science| Physics | 2    | somxt2      | 6                  |
| Science| Physics | 3    | some text 3 | 6                  |
+--------+---------+--------------------+--------------------+
```

1. Where AVG_CHARS_PER_PAGE represents average number of any chars in the TEXT field per TITLE.
2. Keep two TITLEs per TOPIC with the highest number of AVG_CHARS_PER_PAGE

Write close to production code.

```python
def process_topic(df: DataFrame) -> DataFrame:
    # Your code here
    return df
```
