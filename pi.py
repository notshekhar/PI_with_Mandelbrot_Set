from datetime import datetime
PI = 3.14159265359
print(PI)
digits = 7
c = 0.25
e = 1.0 / pow(100, digits-1)
c = c+e
z = 0.0
iteration = 0
d = datetime.now()
while(z<2):
  for i in range(10000):
    if(z<2):
      z = pow(z, 2) + c
      iteration+=1
    else:
      break

  j = "{}".format(iteration)
  k = ""
  diff = digits-len(j)
  if(diff>0):
    for i in range(diff):
      if(i == 0):
        k += "0."
      else:
        k += "0"
    k += j
  else: 
    for i in range(len(j)):
      if(i==0):
        k += "{}.".format(j[i])
      else: 
        k += j[i]
  print(k)

value = k
print("")
print("Total time to calculate: {}".format(datetime.now()-d))
print("Original PI value: {}".format(PI))
print("Calculated PI value: {}".format(value))
print("Error: {}".format(PI - float(value)))
