import day_finder as df

def header():
    col = 1
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    for i in days:
        if col==1:
            print("\n|", end='')
        if col==7:
            col=0
        print(f'\t{i}\t|', end='')
        col+=1

def setup(m, y):
    days = df.find_days(m, y)

    print("\n|", end='')

    col = 1
    for i in range(days+1):
        print(f'\t\t|', end='')
        col+=1
    if col==7:
        print("\n|", end='')
        col=1
    return col

def print_calendar(m, y, col):
    for i in range(1, df.days_in_month(m, y)+1):
        if col==1:
            print("\n|", end='')
        if col>=7:
            # print("\n|")
            col=0
        print(f'\t{i}\t|', end='')

        col+=1

month = int(input("Month: "))
year = int(input("Year: "))

print(f"\nCalendar for {df.find_month(month)}, {year}\n")

header()
print_calendar(month, year, setup(month, year))

print('\n\n')


    


# print("\n------------------------------")