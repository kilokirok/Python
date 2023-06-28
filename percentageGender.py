#CIS 101 Jiyul Seung Problem 11.5
def upper(letter):
  fl=""
  letter=letter.split()
  for i in range(len(letter)):
    if i in range(1,len(letter),2):
      letter[i]=letter[i].upper()
    if not (i in range(1,len(letter),2)):
      letter[i]=letter[i]
  
  for i in range(len(letter)):
    fl=fl+letter[i]+" "
  print fl
        
        

#CIS 101 Jiyul Seung Problem 11.12
def secret(letter):
  pw=""
  for i in letter:
    pw=pw+str(ord(i))
  print pw


#CIS 101 Jiyul Seung Problem 11.18
def percentageGender(letter):  
  print "There are",(1.0*(letter.count('m'))/len(letter)),"males,", (1.0*(letter.count('f'))/len(letter)),"femals."  
  
  
  