#CIS 101 Jiyul Seung

def xy():
  while true:
    print ('to end this program, enter "" as the value for x')
    x = float (input ("Input value for x: "))
    if x == "":
      break
    y = input ("input value for y: ")
    print ("x+y= " , x+y, "x-y= ", x-y, "x*y= ", x*y, "x/y= ", x/y)
  print ("end")
  