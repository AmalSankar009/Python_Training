class MyNum:
  def __iter__(self):
   self.a = 1
   return self

  def __next__(self):
    if self.a <= 5:
       x = self.a
       self.a += 1
       return x
    else:
        raise StopIteration

obj = MyNum()
myiter = iter(obj)

for x in myiter:
 print(x)