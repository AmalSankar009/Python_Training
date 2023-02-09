class add:  
    def __init__(self, X, Y):  
        self.X = X  
        self.Y = Y  
       
    def __add__(self, U):  
        return self.X + U.X, self.Y + U.Y  
       
a1 = add(10, 20)  
a2 = add(5, 15)  
a3 = a1 + a2  
print (a3)  