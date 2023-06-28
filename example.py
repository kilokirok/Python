def txtFile(): 
  path=pickAFile()
  print path
  sCnt = 0
  file=open(path,"rt")
  contents=file.read()
  for i in range(len(contents)):
    if contents[i].lower() == "s":
      sCnt += 1
  print "From " + str(len(contents)) + " total characters, there are " + str(sCnt) + " 'S' or 's' characters."