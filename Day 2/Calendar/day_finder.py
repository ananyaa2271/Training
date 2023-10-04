def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0

def days_in_month(month , year=1990):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30

def date_value(month, year):
    value=0
    y=year-1
    value = y * 365 + y//4  - y//100 + y//400
    m=1
    while m<month:
        value+= days_in_month(m,year)
        m+=1
    return value%7

def find_days(m, y):
    return date_value(m, y)

def find_month(m):
    months = ["January", "February", "March", 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[m-1]
