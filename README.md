# work time tracker

This simple tool is used to track working hours and keep the weekly overhours in control.

## how it works?
The logic of the scipt is following:
- check if the directory `working-hours` exists under your home folder, if not create if with default `755` permissions
- Within the directory it expects the files named in the `YYYY-MM-DD` format ex. `2022-10-10` and contains two timestamps (for start and end time)
- determine number of iteration for the `for` loop using number value of a current weekday
- calculate overhours for current day (if possible - two value in file are needed) and if possible repeat this step for other files from the current week
- present results

Assumption: as the app is desinged to run linux OS I've used the user's home directory (`~`) as reference point for used paths within the code.

# usage

To invoke the script simply call
```shell
python3 main.py
```
It will get current date and generate report for current week based on files located in `~/working-hours/` directory.

## my implementation

To keep track of the current overhours status I've created a two bash functions and aliases (using `~/.bash_aliases` file)
The function `startDay` and `endDay` have one difference - `startDay` create a file if it doesn't exist or truncate it first if file was not empty. The `endDay` only append second timestamp to proper file.

```shell
startDay(){
    date +%s > ~/working-hours/$(date +'%Y-%m-%d')
    python3 ~/scripts/overhours.py
}
alias sd="startDay"

endDay(){
    date +%s >> ~/working-hours/$(date +'%Y-%m-%d')
    python3 ~/scripts/overhours.py
}
alias ed="endDay"
```

### additional improvements

To keep files tidy the logrotate entry will be created - as TODO task.