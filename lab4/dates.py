import datetime


def difference_date(date = datetime.datetime.now(), days=5): 
  return date - datetime.timedelta(days=days)


def print_sibling_days(date = datetime.datetime.now()):
  print("Yesterday:", (date - datetime.timedelta(days=1)).strftime("%A, %d %B %Y, %H:%M:%S"))
  print("Today:", date.strftime("%A, %d %B %Y, %H:%M:%S"))
  print("Tomorrow:", (date + datetime.timedelta(days=1)).strftime("%A, %d %B %Y, %H:%M:%S"))


def drop_microseconds(date):
  return date.replace(microsecond=0)


def seconds_diff(date1, date2):
  return round((abs(date1 - date2)).total_seconds())


