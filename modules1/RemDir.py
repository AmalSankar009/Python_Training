import os 
      
directory = "NewFolder"

parent = "/home/amals/Python_Training/"

path = os.path.join(parent, directory) 
      
os.rmdir(path) 