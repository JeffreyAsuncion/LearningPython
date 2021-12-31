import calendar

def CountDays(theyear, themonth, whichday):
    counter = 0
    weekslist = calendar.monthcalendar(theyear, themonth) # returns the number of weeks
    for week in weekslist:
        if week[whichday] != 0:
            counter += 1
    return counter

run = True
while(run):
    try:
        print("Which day of the week do you want to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or 'exit' to quit")
        theDay = input()

        if theDay.lower() == 'exit':
            run == False
            break

        theYear = int(input("Input the year : "))
        theMonth = int(input("Input the Month : "))
        print(f"There are {CountDays(theYear, theMonth, int(theDay))} day in {theMonth}th month in year {theYear}")
        print("\n\n")
    except Exception as e:
        print(e)
        print("Sorry, not a valid response!")