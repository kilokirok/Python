# CIS 101 Jiyul Seung

def cs():
  while true:
    print
    print 'Enter Name and credit hours ("Name",nch)'
    
    info = input(" #Enter -number for credit hours to finish :  ")
   
    if info[1] <0 :
      print "Mahalo!"
      break
    
    if len(info)== 2 and type (info[0])==str and type (info[1])==int:
      nch=info[1]
      print "Aloha", info[0] ,"you are a",
      if nch < 30: 
        print "Freshman."
      
      elif nch < 60: 
        print "Sophmore."
        
      elif nch < 90: 
        print "Junior."
        
      elif nch < 130: 
        print "Senior."
        
      elif nch >= 130:
        print "graduate."
        
    else:
      print "Incorrect input information."
      
    
        
        
        
        
      
    
    