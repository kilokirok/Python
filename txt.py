#CIS 101 Jiyul Seung  
  
def txt(): 
  way=pickAFile()
  tf=open(way,"rt")
  text=tf.read()
  Act = 0
  act = 0 
  ict = 0
  for i in range(len(text)):
    if text[i] == "A":
      Act += 1
    elif text[i] == "a":
      act += 1
    elif text[i] == "i":
      ict += 1
  print "The file contains",   str(len(text)), "characters," , str(Act), " 'A' characters," , str(act), " 'a' characters, and", str(ict), " 'i'characters." 
  
