
# -- Using the variable called current_datetime, subtract 15 days from the current time.

from datetime import datetime as dt, timedelta

#
current_datetime= dt.today()
# current date formatted 
time_1 = current_datetime.strftime('%d/%m/%Y')

# current minus 15days.
time_2 = current_datetime - timedelta(days=15)
new_date = time_2.strftime('%Y-%m-%d')


print('Current date is:', time_1)
print('new date is: ', new_date)



