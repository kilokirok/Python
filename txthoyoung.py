def txtFile(): 
  path=pickAFile()
  vCnt = 0
  SenCnt = 0
  UCnt = 0
  file=open(path,"rt")
  contents=file.read()
  for i in range(len(contents)):
    if contents[i].lower() in "aeiou":
      vCnt += 1
  for i in range(len(contents)):
    if contents[i] in ".!?":
      SenCnt += 1
  for i in range(len(contents)):
    if contents[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      UCnt += 1
  print "The file contains " , str(len(contents)) , " charecters, " , str(SenCnt) , " sentences " , str(vCnt) , " vowels " + str(UCnt) + " upper case alphabet letters "