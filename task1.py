
# -- Using the variable called current_datetime, subtract 15 days from the current time.

from datetime import datetime as dt, timedelta
# import datetime as dt
# timedelta can be called straight from datetime. or dt. (depending on the import)
# makes it easier this way.

current_datetime= dt.today()
# current date formatted 
time_1 = current_datetime.strftime('%d/%m/%Y')

# current minus 15days.
time_2 = current_datetime - timedelta(days=15)
new_date = time_2.strftime('%Y-%m-%d')


print('Current date is:', time_1)
print('new date is: ', new_date)


# correction  i would need to have only 'import datetime as dt'' above.

current_datetime = dt.datetime.now()

days = dt.timedelta(days=15)
past_date = current_datetime - days
print(past_date.date())

# to have the specific date as mention in the exercice :

current_datetime = '8/07/2021'
new_date = dt.datetime.strptime(current_datetime, '%d/%m/%Y')

days = dt.timedelta(days=15)
past_date = new_date- days
print(past_date.date())