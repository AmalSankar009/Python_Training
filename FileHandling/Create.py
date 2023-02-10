f = open("/home/amals/Python_Training/FileHandling/New.txt", "w")

f.write("New file created by Amal")
f.close()

f = open("/home/amals/Python_Training/FileHandling/New.txt","r")
print(f.read()) 
f.close()

