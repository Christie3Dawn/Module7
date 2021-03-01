# 1. Try the code below and revise it to current time.

from datetime import datetime
from datetime import timedelta


now = datetime.today()
print("The current date and time is: ", now)

print("The current date and time is: {0}/{1}/{2}\t{3}:{4}".format(now.month, now.day, now.year, now.hour, now.minute))


# Using given code
import sys
import datetime

for line in sys.stdin:
    data = line.strip().split("\t")

    now = datetime.datetime.now()   # Local Time (in a datetime.datetime object)

    if len(data) == 4:
        store, item, cost, payment = data
        print("{0}\t{1}\t{2}".format(now.strftime("%m/%d/%Y %I:%M:%S %p"), item, cost))



# 2.  Add the timedelta to the datetime and subtract 60 second and added 2 year .
#     (Hit: timedelta(seconds=60))  For each condition, state the code and output.

print("Adjusted date time (add 2 years, minus 60 sec) is: ", now + timedelta(weeks = 104, seconds = -60))

print("One day added: ", now + timedelta(days = 1))


from datetime import timedelta
#add 1 day


# 3. Create a timedelta object representing 100 days, 10 hours, and 13 minutes.
from datetime import timedelta

d = timedelta(microseconds = -1)

(d.days, d.seconds, d.microseconds)

new = timedelta(days = 100, hours = 10, minutes = 13)
print("Timedelta representing 100 days, 10 hours, and 13 minutes: ", new)




# 4. Write a function that takes two arguments (feet and inches) with this time object

#from datetime import datetime
# get current date

#datetime_object = datetime.now()

#print(datetime_object)

#print('Type: - ', type(datetime_object))

from datetime import datetime
from datetime import timedelta

def distance():
    print()
    feet, inches = eval(input("Enter your distance in (feet, inches): "))
    cfeet = inches * 12
    dfeet = feet + cfeet
    dtimemin = round(dfeet/272.8, 2)
    dtime = datetime.today() + timedelta(minutes = dtimemin)
    print("Your trip will take {0} minutes.".format(dtimemin))
    print("You will arrive at {0} walking that distance.".format(dtime.strftime("%I:%M:%S %p")))

distance()
