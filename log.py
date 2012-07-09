#encoding: utf-8

import sys,re

pattern_hour = re.compile(r'^\(\d{2}:\d{2}\)$')
pattern_day = re.compile(r'^\(\d\d*\+\d{2}:\d{2}\)$')
dictionary = {}

def isUser(user):
  return (not (user == 'reboot') and not (user == 'shutdown') and not (user == 'wtmp'))

def changeTime2Min(time):
  if pattern_hour.match(time):
    index_colon = time.index(':')
    hour = int(time[1:index_colon]) * 60
    min = int(time[index_colon+1:-1])
    return (hour + min)
  elif pattern_day.match(time):
    index_plus = time.index('+')
    index_colon = time.index(':')
    day = int(time[1:index_plus]) * 24 * 60
    hour = int(time[index_plus:index_colon]) * 60
    min = int(time[index_colon+1:-1])
    return (day + hour + min)

def insert2dictionary(user,time):
  dictionary[user] = dictionary.get(user,0) + time
  
for line in sys.stdin:
  row = line.strip().split(' ')
  user = row[0]
  time = row[-1]
  time = changeTime2Min(time)
  if isUser(user) and time:
    insert2dictionary(user,time)
for user,time in dictionary.items():
  print "%s = %d(min)" % (user,time)
