#CIS 101 Jiyul Seung  

def textRectagle(char, width, height):
  for i in range(height):
    print char*width
    
  print "     "
  print "     "
    
  print char*width
  for q in range(height-2):
    print char+" "*(width-2)+char
  print char*width
  
  print "     "
  print "     "
  
  
  for w in range (0, width):
    print char*(width-w) + " " *(w)+char 
  if width > height:        
    print char*width + char 
  else:        
    for r in range (height-width): 
      print char*width + char
  
  
  
  
  
  