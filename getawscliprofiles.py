#!/usr/bin/python
import os

start = 'profile "'
end = '"]'
aws_config_path = os.path.expanduser('~/.aws/')
f = open(aws_config_path + "config","r")
for x in f:
  if '[profile "' in x:
    print x[x.find(start)+len(start):x.rfind(end)]
  elif '[default]' in x:
    print('default')