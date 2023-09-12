
# -- Your task is to write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.


from datetime import datetime, timedelta


current_date = datetime(year=2020, month=1, day=1)

due_date = current_date + timedelta(days=25)

customer_name = 'Friedrich'


print('hello,', customer_name, 'your rent of 300 euros is due on', due_date.strftime('%d %B, %Y'))

