daysPerMonth = { 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }
daysOfWeek = { 0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday' }
year, month, day, dow = 0, 1, 2, 3



def isLeapYear(x):
    """
    >>> isLeapYear(1904)
    True
    >>> isLeapYear(1900)
    False
    >>> isLeapYear(2000)
    True
    """
    if x % 4 == 0:
        if x % 100 == 0 and x % 400 != 0:
            return False
        return True
    return False

def nextMonth(date):
    """
    >>> nextMonth((2010, 1, 1, 5))
    (2010, 2, 1, 1)
    >>> nextMonth((2012, 2, 1, 3))
    (2012, 3, 1, 4)
    >>> nextMonth((1999, 12, 1, 3))
    (2000, 1, 1, 6)
    """
    daysInMonth = 0
    if date[month] == 2 and isLeapYear(date[year]):
        daysInMonth = 29
    else:
        daysInMonth = daysPerMonth[date[month]]

    newDayOfWeek = (date[dow] + daysInMonth) % 7
    newMonth = (date[month] % 12) + 1
    newYear = date[year]
    if newMonth == 1:
        newYear = newYear + 1

    return (newYear, newMonth, 1, newDayOfWeek)

def printDate(date):
    print(str(date[year]) + '.' + str(date[month]) + '.' + str(date[day]) + ', ' + str(daysOfWeek[date[dow]]))


def findAnswer():
    startDate = (1900, 1, 1, 1)
    while startDate[year] == 1900:
        startDate = nextMonth(startDate)

    print('Starting Date is:')
    printDate(startDate)

    count = 0
    curDate = startDate
    while curDate[year] < 2001:
        if curDate[dow] == 0:
            printDate(curDate)
            count = count + 1
        curDate = nextMonth(curDate)

    print('Found ' + str(count) + ' months starting on Sunday')

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
