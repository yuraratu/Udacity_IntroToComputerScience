###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###


def isLeapYear(year):
    """
    Return True for leap year and False for common
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def daysInMonth(year, month):
    """
    Return number of days in a month
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28


def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2:
        return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    # program defensively! Add an assertion if the input is not valid!
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        (year1, month1, day1) = nextDay(year1, month1, day1)
        days += 1
    return days


# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed", '| result:', result, '| answer:', answer)
        else:
            print("Test case passed!", '| result:', result, '| answer:', answer)
test()
