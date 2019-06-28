from datetime import datetime

digits = 9
c = 0.25
e = 1.0 / pow(100, digits-1)
c = c+e
z = 0
iteration = 0
d = datetime.now()
while(z<2):
  for i in range(100000):
    if(z<2):
      z = pow(z, 2) + c
      iteration+=1
    else:
      break


print(datetime.now()-d)
print(iteration)
