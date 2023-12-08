
import datetime
name = "Garima"
date = datetime.date.today()

# print(date)

letter ='''Dear {0}
You are selected!
{1}'''.format(name,date)

print(letter)