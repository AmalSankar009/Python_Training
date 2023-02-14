class plus:
    __ctr = 0   #__ makes pvt
 
    def sum(self):
        self.__ctr += 1
        print(self.__ctr)
 
 
count = plus()
count.sum()
count.sum()
 
print(count._plus__ctr)