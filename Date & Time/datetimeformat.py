from datetime import datetime
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))
current_date_time = datetime.now()
print(current_date_time)
print(datetime.now().year)
print(current_date_time.year)
print(current_date_time.month)
print(current_date_time.day)
print('{:%Y-%m-%d %H:%M}'.format(current_date_time))
print(type(current_date_time))
# strftime converts a datetime object into string provided a format
date_time_in_str = datetime.strftime(current_date_time, "%Y-%m-%d %H:%M")
print(date_time_in_str)
print(type(date_time_in_str))
str_current_date_time = str(current_date_time)
print(str_current_date_time)
# strptime parses a string and returns a datetime object provided a format
print(datetime.strptime(date_time_in_str, "%Y-%m-%d %H:%M"))