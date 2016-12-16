import random

a = []
n = 100
for i in range(n):
    x = random.randint(1, 100)
    a.append(x)
print(a)

max = a[0]
for x in a:
    if max < x:
        max = x

for i in range(0, len(a)):
     if max < a[i]:
         max2 = a[i]

print("max = {0}".format(max))