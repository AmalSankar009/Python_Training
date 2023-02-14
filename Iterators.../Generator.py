def PowerTwo(m=0):
   n=1
   while n < m:
       yield 2 ** n
       n+=1

a = PowerTwo(10)

for i in a:
   print(i)