class school:
  def __init__(self, name, std):
    self.name = name
    self.std = std
  def disp(self):
    print(self.name)
    print(self.std)   

st = school("Amal", 10)
st.disp()
