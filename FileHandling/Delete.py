import os
if os.path.exists("New.txt"):
  os.remove("New.txt")
  print("Deleted")
else:
  print("The file does not exist") 