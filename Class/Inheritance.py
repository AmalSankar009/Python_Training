class school:
  def __init__(self, name, std):
    self.name = name
    self.std = std
  def disp(self):
    print(self.name)
    print(self.std)   

class mark:
  def __init__(self,sub,mrk):
     self.sub=sub
     self.mrk=mrk
  def disp1(self):
    print(self.sub)
    print(self.mrk) 


class student(school,mark):
  pass

st = student("Amal", 10)
st.disp()
#st.disp1()
