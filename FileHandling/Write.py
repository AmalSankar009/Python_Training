f = open("/home/amals/Python_Training/FileHandling/PythonTXT","w")
f.write("Good Morning")
f.close()

f = open("/home/amals/Python_Training/FileHandling/PythonTXT","r")
print(f.read()) 
f.close()