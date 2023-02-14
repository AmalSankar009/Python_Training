import os
f = open("New1.txt", "w")

f.write("New file created by Amal")
f.close()

f = open("New1.txt","r")
print(f.read()) 
f.close()

 
#print('File name :    ', os.path.basename("New.txt"))
#print('Directory Name:{}    '.format(os.path.dirname("New.txt")))
#print(type( os.path.dirname("New.txt")))