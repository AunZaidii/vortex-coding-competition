n = int(input("Enter number of people: "))
k = int(input("Enter position: "))
people = []
served = []
notserved = []
for i in range(0,n):
  people.append(i+1)

a = 1
while (a < len(people)):
  served.append(a)
  a = a+a+1
j = 0

if k in served:
  print("Yes")   
else:
  print("No")

for k in range(len(people)):
  if k not in people:
    notserved.append(k)
print(notserved)