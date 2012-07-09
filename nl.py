# conding: UTF-8
import sys

def getLineList(argv):
  f = open(sys.argv[len(argv) - 1],'rU')
  line_list = f.readlines()
  f.close()
  line_list[-1] = line_list[-1].rstrip()
  return line_list

def noOption(line_list):
  index = 1
  for line in line_list:
    if not line.isspace():
      print "%6d %s" % (index,line),
      index += 1
    else:
      print line,
  print
 
def zeroPading(line_list):
  index = 1
  for line in line_list:
    if not line.isspace():
      print "%06d %s" % (index,line),
      index += 1
    else:
      print line,
  print

def countSpace(line_list):
  index = 1
  for line in line_list:
    print "%6d %s" % (index,line),
    index += 1
  print

if len(sys.argv) == 2:
  line_list = getLineList(sys.argv)
  noOption(line_list)
elif len(sys.argv) == 3:
  if sys.argv[1] == '-nrz':
    line_list = getLineList(sys.argv)
    zeroPading(line_list)
  elif sys.argv[1] == '-ba':
    line_list = getLineList(sys.argv)
    countSpace(line_list)
