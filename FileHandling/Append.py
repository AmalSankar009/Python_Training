f = open("/home/amals/Python_Training/FileHandling/pyth.txt","a")
f.write("I am from Kochi")
f.close()

f = open("/home/amals/Python_Training/FileHandling/pyth.txt","r")
print(f.read()) 

f.close()