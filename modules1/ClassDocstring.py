class school:
  '''Class School'''  
  def __init__(self, name, std):
    '''Constructor for class school'''
    self.name = name
    self.std = std
  def disp(self):
    '''Function to display'''
    print(self.name)
    print(self.std)   

help(school.disp)
st = school("Amal", 10)
print(st.__doc__)
# st.disp()
