#!/usr/bin/python3

import sys
import os
from datetime import datetime
from datetime import timedelta

if(len(sys.argv) == 1): 
  print('Enter a bank file.')
  sys.exit()

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


filename = sys.argv[1]

if not filename.endswith('.txt'):
  filename += '.txt'

print(filename)
print()

filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
file = open(filepath, "r")

lines = file.readlines()

starts = []
ends = []
extras = []
elapseds = []
absents = 0

for line in lines:
  line = line.strip()

  #-----------------------------------------------------------------------------
  if len(line) < 22:
    # This means line is not full: date, time in, time out

    if len(line) == 12:
      isAbsent = line.split(' ')[1] == '-'
      if(isAbsent):
        absents +=1
        continue

    if len(line) == 16: 
      # This means line has date and time in only
      time = datetime.strptime(line.split(' ')[1], timeFormat)
      strTime = datetime.strftime(addTime(time, 510), timeFormat)

      print (line)
      print('Time in:  {}'.format(line.split(' ')[1]))
      print('Time out: {}'.format(strTime))
    continue
  #-----------------------------------------------------------------------------

  date = line.split(' ')[0]

  startTime = line.split(' ')[1]
  endTime = line.split(' ')[2]


  delta = timedelta(hours=8, minutes=30)

  start = datetime.strptime(startTime, timeFormat)
  end = datetime.strptime(endTime, timeFormat)
  elapsed = (end - start)

  extraTime = timeDeltaFormated(elapsed, delta)

  extras.append(extraTime)

  elapsedString = '{:02d}:{:02d}'.format(int(str(elapsed).split(':')[0]), int(str(elapsed).split(':')[1]))

  print ('{} -> {}'.format(line, elapsedString))

delta = addExtras(extras)

formated = (delta.days*1440) + delta.seconds/60

print('General bank: {:.0f} minutes'.format(formated))
print('Faltas: {}'.format(absents))
