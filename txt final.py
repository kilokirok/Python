# CIS 101 Jiyul Seung

def txt():
  file = ""
  while file != "quit":
    file = input("Enter path and file name (with qutes): ")
    if file == "quit":
      print "Program ended.."
      break
    
     
    
    file  = open(file,"rt")
    content = file.read()
    
    ns = 0    
    nch = 0
    nco = 0
    nl = 0
    
    st = content.split("\n")
    
    for j in st:
      ns += 1    
    js = len(st) - 1
    
    nch = len(content)
    
    for j in content:
      if j.upper() not in "AEIOU" and ord(j.upper()) in range (65,91,1):
        nco += 1 
        
      if ord (j.upper()) in range(65,91,1):
        nl += 1
        
    print "The file contains", js, "lines,", nch, "characters,", nco, "consonants and", nl, "letters."
    