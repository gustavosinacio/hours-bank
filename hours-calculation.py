#!/usr/bin/python3

import os
from datetime import datetime
from datetime import timedelta

def timeDeltaFormated(elapsed, delta):
  if elapsed > delta:
    return ('+', (elapsed - delta));
  else :
    return ('-', (delta - elapsed));

def addExtras(extras):
  time = timedelta(0)
  for extra in extras:
    if extra[0] == '+':
      time += extra[1]
    if extra[0] == '-':
      time -= extra[1]

  return time

file = open('bank.txt', "r")

lines = file.readlines()

starts = []
ends = []
extras = []
elapseds = []

for line in lines:

  if len(line) < 33:
    break

  startString = line[:-1].split(' ')[0]
  endString = line[:-1].split(' ')[1]

  delta = timedelta(hours=8, minutes=30)
  day = startString.split('T')[0]
  start =  datetime.strptime(startString, '%Y-%m-%dT%H:%M')
  end =  datetime.strptime(endString, '%Y-%m-%dT%H:%M')
  elapsed = (end - start)

  extraTime = timeDeltaFormated(elapsed, delta)

  # starts.append(start)
  # ends.append(end)
  # elapseds.append(elapsed)

  extras.append(extraTime)

delta = addExtras(extras)

formated = (delta.days*1440) + delta.seconds/60

print("{:.0f} minutes".format(formated))
