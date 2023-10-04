date = input("Enter date : ").split("/")

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = int(date[0])
month = int(date[1])
year = int(date[2])

days = 0

days = (year - 2001 - 1)*365%7
# print("after year: ", days)

for i in range(2001, year+1):
    if i%100 == 0 and i%4==0:
        if i == year:
            if month>2:
                days+=1
        else:
            days+=1
    elif i%4==0:
        if i == year:
            if month>2:
                days+=1
        else:
            days+=1

# print("after leap: ", days)

for i in range(1, month):
    days += months[i-1]%7

# print("after month: ", days)

days +=day%7
days = days%7

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(days)

print(day_list[days])

