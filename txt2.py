#CIS 101 Jiyul Seung

def txt(): 
  way=pickAFile()
  tf=open(way,"rt")
  text=tf.read()
  marks = 0
  vowels = 0 
  up = 0
 
  for i in range(len(text)):
    if text[i] in ".!?":
      marks += 1
    elif text[i].upper() in "AEIOU":
      vowels += 1
  for w in range(len(text)):    
    if text[w] in "ABCDEFGHIJKLMNOPQRSTUWXYZ":
      up += 1
   
      
    
  print "The file contains",   str(len(text)), "characters," , str(marks), " sentences, " , str(vowels), " vowels, and", str(up), " upper case alphabet letters." 
  tf.close()
  