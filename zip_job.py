#!/usr/bin/env python
import os
from zipfile import ZipFile

array = ["a", "b", "c", "d"]
os.environ['VERSION'] = "1.2.0"
USER = os.getenv('VERSION')

for x in array:
  try:
    f= open(x + ".txt","w")
    f.write("Hello From " + x + " TXT File")
  except IOError:
    print("File not accessible")
  finally:
    f.close()
  try:
    zipObj = ZipFile(x + '_'+ USER + '.zip', 'w')
  except IOError:
    print("Zip not accessible")
  finally:
    zipObj.write(x + '.txt')
