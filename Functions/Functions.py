def fun(x):
  return 5 * x

print(fun(3))
print(fun(5))
print(fun(9))


def funmap(a, b):
  return a + b

x = map(funmap, (10,20,30), (5,10,15)) 
print (list(x))





def funlam(n):
   return lambda a : a * n

multi =funlam(3)

print(multi(10))