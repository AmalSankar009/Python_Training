import os 
      
directory = "NewFolder"
      
parent_dir = "/home/amals/Python_Training"
    
path = os.path.join(parent_dir, directory) 
      
os.makedirs(path) 