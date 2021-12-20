The src folder contains a .py file with the source code used on the National Register Processed Dataset. This Python script creates four separate counters that count the properties by state, category, area of significance, and year listed on the National Register. The script then writes the dictionaries produced by these counters to four separate .csv files. 

The data in the resulting .csv files is formatted as follows:

**Count by Area of Significance** (53 rows, 2 columns)
Column 1: Area of Significance<br>
Column 2: Count

**Count by Category** (6 rows, 2 columns)
Column 1: Category of Property<br>
Column 2: Count

**Count by State** (62 rows, 2 columns)
Column 1: State<br>
Column 2: Count

**Count by Year Listed** (57 rows, 2 columns)
Column 1: Year Listed<br>
Column 2: Count
