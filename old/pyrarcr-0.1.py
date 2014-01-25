#!/usr/bin/env python3

#finds the password of a desired rar or zip file using a brute-force algorithm
##will fail to find the password if the password has a character that isnt in
##the english alphabet or isnt a number (you can change the char. list though)

#importing needed modules
import time,os,sys,shutil

#checking if the user has unrar/p7zip installed
for which in ["unrar","p7zip"]:
 if not shutil.which(which):
  print("ERROR:",which,"isn't installed.\nExiting...")
  sys.exit(-1)

#defining the function
def rc(rf):
 alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890"
 start=time.time()
 tryn=0
 for i in range(sys.maxsize):
  a=[x for x in alphabet]
  for j in range(i):
   a=[x+i for x in alphabet for i in a]
  for k in a:
   if rf[-4:]==".rar":
    print("Trying:",k)
    kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="All OK\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      time.sleep(2)
      sys.exit(1)
   elif rf[-4:]==".zip" or rf[-3:]==".7z":
    print("Trying:",k)
    kf=os.popen("7za t -p%s %s 2>&1|grep 'Everything is Ok'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="Everything is Ok\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      time.sleep(2)
      sys.exit(1)
   else:
    print("ERROR: File isnt a RAR, ZIP or 7z file.\nExiting...")

#checking if the file exists/running the function
if len(sys.argv)==2:
 if os.path.exists(sys.argv[1])==True:
  rc(sys.argv[1])
 else:
  print("ERROR: File doesn't exist.\nExiting...")
else:
 print("Usage:",os.path.basename(__file__),"[rar file]")
 print("Example:",os.path.basename(__file__),"foobar.rar")
