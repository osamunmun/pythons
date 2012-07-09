#coding: utf-8

import glob,sys,os,stat,re,pwd,time

def checkmod(path):
  if os.path.isdir(path):
    permission = 'd'
  else:
    permission = '-'
  mode = stat.S_IMODE(os.lstat(path)[stat.ST_MODE])
  for who in 'USR','GRP','OTH':
    for what in 'R','W','X':
      if mode & getattr(stat,'S_I'+what+who):
        permission = permission+what.lower()
      else:
        permission = permission+'-'
    if mode & getattr(stat,'S_ISVTX'):
      permission = permission[:-1] + 't'
  return permission

def print_normal(filelist):
  for i in filelist:
    print i,
      
def print_i_option(filelist):
  for i in filelist:
    file_stat = os.lstat(i)
    inode = file_stat[stat.ST_INO]
    print inode,i,

def print_l_option(filelist):
  for i in filelist:
    file_stat = os.lstat(i)
    link_num = file_stat[stat.ST_NLINK]
    owner = pwd.getpwuid(file_stat.st_uid)[0]
    group = pwd.getpwuid(file_stat.st_uid)[0]
    filesize = file_stat[stat.ST_SIZE]
    updated_at = time.strftime("%b %e %R", time.localtime(file_stat[stat.ST_MTIME]))
    print checkmod(i),link_num,owner,group,filesize,updated_at,i

if len(sys.argv) == 1:
  filelist = glob.glob('*')
  print_normal(filelist)
elif len(sys.argv) == 2:
  if not re.match(r'^-.$',sys.argv[1]):
    if os.path.isdir(sys.argv[1]):
      os.chdir(sys.argv[1])
      filelist = glob.glob('*')
      print_normal(filelist)
    else:
      filelist = glob.glob(sys.argv[1])
      print_normal(filelist)
  elif re.match(r'^-l$',sys.argv[1]):
    filelist = glob.glob('*')
    print_l_option(filelist)
  elif re.match(r'^-a$',sys.argv[1]):
    filelist = ['.','..']
    filelist = filelist + glob.glob('.*')
    filelist = filelist + glob.glob('*')
    print_normal(filelist)
  elif re.match(r'^-i$',sys.argv[1]):
    filelist = glob.glob('*')
    print_i_option(filelist)
elif len(sys.argv) == 3:
  if sys.argv[1] == '-l':
    if os.path.isdir(sys.argv[2]):
      os.chdir(sys.argv[2])
      filelist = glob.glob('*')
      print_l_option(filelist)
    else:
      filelist = glob.glob(sys.argv[2])
      print_l_option(filelist)
  if sys.argv[1] == '-a':
    if os.path.isdir(sys.argv[2]):
      os.chdir(sys.argv[2])
      filelist = ['.','..']
      filelist = filelist + glob.glob('.*')
      filelist = filelist + glob.glob('*')
      print_normal(filelist)
    else:
      filelist = glob.glob(sys.argv[2])
      print_normal(filelist)
  if sys.argv[1] == '-i':
    if os.path.isdir(sys.argv[2]):
      os.chdir(sys.argv[2])
      filelist = glob.glob('*')
      print_i_option(filelist)
    else:
      filelist = glob.glob(sys.argv[2])
      print_i_option(filelist)
