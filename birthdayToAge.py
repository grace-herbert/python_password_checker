import datetime
from datetime import date


today = date.today()
print("Today's date:", today)


birth_year = (int)(input("What year were you born? "))
birth_month = (int)(input("What month were you born? "))
birth_day = (int)(input("What day in that month were you born? "))

birthday = datetime.datetime(birth_year,  birth_month, birth_day)
if (today.month & today.day) < (birthday.month & birthday.day): minus_year = True 
if minus_year: age = today.year -1 - birthday.year 
else: age = today.year - birthday.year
  

print("You were born in  "+ str(birth_year) + " and so you are " + str(age) + ".")