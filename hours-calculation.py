#!/usr/bin/python3

import os
from datetime import datetime
from datetime import timedelta

dateFormat = '%Y-%m-%dT%H:%M'
printFormat = '%H:%M'

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

  if len(line) < 33:
    line = line.strip()

    if len(line) == 16: # ------------------------------------------------------
      time = datetime.strptime(line, dateFormat)
      strTime = datetime.strftime(addTime(time, 510), printFormat)
      print('Time in:  {}'.format(line.split('T')[1]))
      print('Time out: {}'.format(strTime))
    # --------------------------------------------------------------------------
    break

  startString = line[:-1].split(' ')[0]
  endString = line[:-1].split(' ')[1]

  delta = timedelta(hours=8, minutes=30)
  day = startString.split('T')[0]
  start = datetime.strptime(startString, dateFormat)
  end = datetime.strptime(endString, dateFormat)
  elapsed = (end - start)

  extraTime = timeDeltaFormated(elapsed, delta)

  # starts.append(start)
  # ends.append(end)
  # elapseds.append(elapsed)

  extras.append(extraTime)

delta = addExtras(extras)

formated = (delta.days*1440) + delta.seconds/60

print('General bank: {:.0f} minutes'.format(formated))
