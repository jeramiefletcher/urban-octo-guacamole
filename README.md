# workingdays Package

python package of date functions/utilities centered around workday calculations.

## dateCleanup

All of the "workingday" functions first pass through the "dateCleanup" utility before executing. The dateCleanup converts a string to datetime (y, m, d, h, M, s). It can convert alpha numeric, German date formats, timestamps with separators (":"" or "-"), timestamps without spaces between date and time ('YYYY-MM-DDhh:mm:ss' to 'YYYY-MM-DD hh:mm:ss' or 'YYYY:MM:DDhh:mm:ss' to 'YYYY-MM-DD hh:mm:ss'), or datetime with no separators.

The "datevalue" is expected to be Type string unless epoch=True, Then datevalue expected to be Type Int.

## workday

Returns a string ("%Y%m%d") of the workingday based off the offset. Optional Holidays can be passed.

## workdayStart

Returns a string ("%Y%m%d") of the workingstart based off the offset. Optional Holidays can be passed.

## compareWorkingdays

Returns the days (Int) between two working dates. Optional Holidays can be passed.

## lastWorkdayOfMonth

Returns a string ("%Y%m%d") of the last workingday of the month. Optional Holidays can be passed.

## lastWorkdayOfQtr

Returns a string ("%Y%m%d") of the lastWorkdayofQtr. Optional Holidays can be passed. Default qtrs are based off "Calendar Years", but Optional kwarg can change the Qtr "Months" (Can be a list or dict).

example:

``` python
quarters =  {"Q1": ["Nov", "Dec", "Jan"],
             "Q2": ["Feb", "Mar", "Apr"],
             "Q3": ["May", "Jun", "Jul"],
             "Q4": ["Aug", "Sep", "Oct"]}

lastWorkdayOfQtr('20200213', key=quarters)
```

Results

     '20200430'

## lastDayOfMonth

Returns a string ("%Y%m%d") of the lastDayOfMonth.
