# workingdays Package:
python package of date functions/utilities centered around workday calculations.


## dateCleanup

All of the "workingday" functions first pass through the "dateCleanup" utility before executing. The dateCleanup converts a string to datetime (y, m, d, h, M, s). It can convert alpha numeric, German date formats, timestamps with seperators (":"" or "-"), timestamps without spaces between date and time ('YYYY-MM-DDhh:mm:ss' to 'YYYY-MM-DD hh:mm:ss' or 'YYYY:MM:DDhh:mm:ss' to 'YYYY-MM-DD hh:mm:ss'), or datetime with no seperators.

The "datevalue" is expected to be Type string unless epoch=True, Then datevalue expected to be Type Int.


## workday
Returns a string ("%Y%m%d") of the workingday based off the offset. Optionial Holidays can be passed.

## workdayStart
Returns a string ("%Y%m%d") of the workingstart based off the offset. Optionial Holidays can be passed.

## compareWorkingdays
Returns the days (Int) between two working dates. Optionial Holidays can be passed.

## lastWorkdayofMonth
Returns a string ("%Y%m%d") of the last workingday of the month. . Optionial Holidays can be passed.

## lastWorkdayofQtr
Returns a string ("%Y%m%d") of the lastWorkdayofQtr. Optionial Holidays can be passed. Default qtrs are based off "Calendar Years", but Optional kwarg can change the Qtr "Months" (Can be a list or dict).

example:
``` python
quarters =  {"Q1": ["Nov", "Dec", "Jan"],
             "Q2": ["Feb", "Mar", "Apr"],
             "Q3": ["May", "Jun", "Jul"],
             "Q4": ["Aug", "Sep", "Oct"]}

lastWorkdayofQtr('20200213', key=quarters)
```
Results

     '20200430'

## lastDayofMonth
Returns a string ("%Y%m%d") of the lastDayofMonth.
