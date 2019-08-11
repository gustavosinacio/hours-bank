#!/usr/bin/python3

import sys
import os
from datetime import datetime
from datetime import timedelta

print(sys.argv)

timeFormat = '%H:%M'

def timeDeltaFormated(elapsed, delta):
  if elapsed > delta:
    return ('+', (elapsed - delta));
  else :
    return ('-', (delta - elapsed));

def addTime(time, addminutes):
  return (time + timedelta(minutes=addminutes))

def addExtras(extras):
  time = timedelta(0)
  for extra in extras:
    if extra[0] == '+':
      time += extra[1]
    if extra[0] == '-':
      time -= extra[1]

  return time

filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bank.txt')
file = open(filepath, "r")

lines = file.readlines()

starts = []
ends = []
extras = []
elapseds = []

for line in lines:

  if len(line) < 23:
    line = line.strip()

    if len(line) == 16: # ------------------------------------------------------
      time = datetime.strptime(line.split(' ')[1], timeFormat)
      strTime = datetime.strftime(addTime(time, 510), timeFormat)
      print('Time in:  {}'.format(line.split(' ')[1]))
      print('Time out: {}'.format(strTime))
    # --------------------------------------------------------------------------
    break

  date = line[:-1].split(' ')[0]

  startTime = line[:-1].split(' ')[1]
  endTime = line[:-1].split(' ')[2]

  delta = timedelta(hours=8, minutes=30)

  start = datetime.strptime(startTime, timeFormat)
  end = datetime.strptime(endTime, timeFormat)
  elapsed = (end - start)

  extraTime = timeDeltaFormated(elapsed, delta)

  extras.append(extraTime)

delta = addExtras(extras)

formated = (delta.days*1440) + delta.seconds/60

print('General bank: {:.0f} minutes'.format(formated))
