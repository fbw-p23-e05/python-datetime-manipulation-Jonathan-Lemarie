
# -- Your task is to write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.

import datetime as dt


current_date = dt.datetime(year=2020, month=1, day=1)

due_date = current_date + dt.timedelta(days=25)

customer_name = 'Friedrich'


print('hello', customer_name, 'your rent of 300 euros is due on', due_date.strftime('%d %B, %Y'))

# correction below, another way to do it.

rent_text = due_date.strftime('%d %B, %Y')
print(f'Hello Friedrich, your rent of 300 € is due on {rent_text}')