# work time tracker

Simple tool to save start and end timestamp, then based on that values calculate the weekly overhours status.

# usage

using bash_aliases file the two functions associated with proper aliases are used to save timestamps and generate raport
`sd` as acronim of `start day` is used to generate start timestamp (in seconds since epoch) stored in `~/wh/<date>.log` (`wh` is an acronim of `working hours`)
`ed` is an acronim of `end day` and is used to generate the end timestamp. Beside that it triggers the python script which compare the timestamps and generate raport.

## structure of a data files
The app checks if the `~/working-hours` directory exists and if not, creates it with the `755` permissions.
Within the directory it expects the files named in the `YYYY-MM-DD` format ex. `2022-10-10`

The file should contains two lines - first with the start timestamp (followed by the new line character) and the second one with end timestamp ex.
```text
1665385121
1665414065
```
