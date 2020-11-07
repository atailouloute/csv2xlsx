# CSV2XLSX

# Description
A simple tool written in Python, single file executable to convert CSV files to XLSX.

# The binaries

The compiled binaries could be found here:
```
dist/csv2xlsx_linux_amd64
```

# Usage

The script have multiple options, here is the list of available options:

| Option  |  Required | Default value  |  Description |
|---|---|---|---|
| input_file  | ✔️ |   |   The input CSV file |
| output_file  | ✔️  |   |  The destination output XLSX file  |
| delimiter  |   | ","  |  The delimiter for the CSV  |
| override  |   | False  | Whether to override or not the destination | 
| show_progress  | | False | Show the conversion progress bar  |

# Example

```bash
$ csv2xlsx --input_file=input.csv --output_file=output.xlsx --show_progress=True

Converting 1000 lines: 100%|███████████████████████████████████████████████████████▉| 1000/1000 [00:02<00:00, 500 line/s]
```

# Authors
* Ahmed TAILOULOUTE <ahmed.tailouloute@gmail.com>