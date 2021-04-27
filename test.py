import numpy as np

e = [i for i in range(-15, 15)]
r=[]
for i in e:
    if i < 0:
        r.append(0)
    else:
        r.append(i)

print(e)
del (e)
print(e)
print(r)