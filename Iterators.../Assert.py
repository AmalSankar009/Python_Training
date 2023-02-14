#The assert keyword test if a condition in the code returns True, if not, the program will raise an AssertionError.

def Positive(x):
   assert (x >= 0),"Negative"
   return x*x

print (Positive(10))
print (Positive(-5))