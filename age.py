# coding: UTF-8
import sys
import re
import datetime
from datetime import timedelta,date

month_dictionary = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
today = datetime.datetime.today().strftime('%Y%m%d')
today_month = datetime.datetime.today().strftime('%m')
today_day = datetime.datetime.today().strftime('%d')
today_year = datetime.datetime.today().strftime('%Y')

def calcRemainMonthWithDelim(delimiter):
  age_year = (int(today) - int(''.join(birthday.split(delimiter))))/10000
  birthday_year = birthday.split(delimiter)[0]
  birthday_month = int(birthday.split(delimiter)[1])
  birthday_day = int(birthday.split(delimiter)[2])
  year_diff_with_month = (int(birthday_month)- int(today_month))
  return calcRemainUtil(age_year,birthday_year,birthday_month,birthday_day,year_diff_with_month)

def calcRemainMonth():
  age_year = (int(today) - int(birthday))/10000
  birthday_year = int(birthday[:4])
  birthday_month = int(birthday[4:6])
  birthday_day = int(birthday[6:])
  year_diff_with_month = birthday_month - int(today_month)
  return calcRemainUtil(age_year,birthday_year,birthday_month,birthday_day,year_diff_with_month)

def calcRemainUtil(age_year,birthday_year,birthday_month,birthday_day,year_diff_with_month):
  if 0 < year_diff_with_month:
    next_birthday = datetime.date(int(today_year),int(birthday_month),int(birthday_day))
    remain_days = next_birthday - date.today()
    return age_year, year_diff_with_month,remain_days.days
  elif year_diff_with_month == 0:
    year_diff_with_day = birthday_day - int(today_day)
    if year_diff_with_day > 0:
      next_birthday = datetime.date(int(today_year),int(birthday_month),int(birthday_day))
      remain_days = next_birthday - date.today()
      return age_year, 12,remain_days.days
    elif year_diff_with_day == 0:
      print "Happy Birthday!"
      exit()
    else:
      next_birthday = datetime.date(int(today_year)+1,int(birthday_month),int(birthday_day))
      remain_days = next_birthday - date.today()
      return age_year, year_diff_with_month,remain_days.days
  else:
    next_birthday = datetime.date(int(today_year)+1,int(birthday_month),int(birthday_day))
    remain_days = next_birthday - date.today()
    return age_year, year_diff_with_month + 12, remain_days.days

def printMessageWithDelim(delimiter):
  age = calcRemainMonthWithDelim(delimiter)
  print "You are %d(and %s months)years old" % (age[0], age[1])
  print "Your next birthday is %d days later" % (age[2])

def printMessage():
  age = calcRemainMonth()
  print "You are %d(and %s months)years old" % (age[0], age[1])
  print "Your next birthday is %d days later" % (age[2])

if len(sys.argv) == 2:
  birthday = sys.argv[1]
elif len(sys.argv) == 4:
  birthday = sys.argv[3],month_dictionary[sys.argv[2]],sys.argv[1]
  birthday = ''.join(birthday)
if re.match(r'^\d{4}/\d{2}/\d{2}$',birthday):
  delimiter = '/'
  printMessageWithDelim(delimiter)
elif re.match(r'^\d{4}-\d{2}-\d{2}$',birthday):
  delimiter = '-'
  printMessageWithDelim(delimiter)
elif re.match(r'^\d{8}$',birthday):
  printMessage()
