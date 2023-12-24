import random, datetime


def get_dates(n):
    dates = []
    count = n
    while(count):
        try:
            date = datetime.date(random.randint(2000,2025), random.randint(1,12), random.randint(1,31))
            dates.append(date)
            count-=1
        except ValueError:
            continue
    return dates

def check_dates(dates):
    for i in range(len(dates)):
        for j in range(i+1,len(dates)):
            if (dates[i].month == dates[j].month) and (dates[i].day == dates[j].day):
                return 1
    return 0

def main():
    birthdates = int(input("\nHow many birthdays should I generate?"))
    count = 0
    for i in range(100_000):
        dates = get_dates(birthdates)
        if(check_dates(dates)):
            count+=1
        if(i%10_000 == 0 and i != 0):
            print(f"{i} simulations run ....")
    print(f'''\nOut of 100,000 simulations of {birthdates} people, there was a matching birthdate in that group
atleast {count} times. This means that {birthdates} people have a {count/100_0}% chance of having a matching birthday
in their group.''')

main()
        