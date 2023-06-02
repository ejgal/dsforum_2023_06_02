Parquet
- Kolonnebasert filformat - delt opp i rad-grupper
- Innebygd statistikk per kolonne per rad-gruppe
- Typer
- Kompresjon
- Minnebruk
    - Kan lese enkelte kolonner
    - Slipper å lese inn data for så å konvertere typer
- Binært

DuckDB
- Embedded - kjører som en del av applikason / script
- OLAP database
    - Kolonneorientert
    - Få (men tunge) spørringer
- Litt som sqlite
    - for analyse


- Data import & export
- Documentation -> Client APIs

- [Querying Parquet](https://duckdb.org/2021/06/25/querying-parquet.html)
- [Choosing a good file format for Pandas](https://pythonspeed.com/articles/best-file-format-for-pandas/)
- [The fastest way to read a CSV in Pandas](https://pythonspeed.com/articles/pandas-read-csv-fast/)
- [DuckDB Docs](https://duckdb.org/docs/)
- [5 minute introduction to DuckDB](https://shekhargulati.com/2019/12/15/the-5-minute-introduction-to-duckdb-the-sqlite-for-analytics/)
