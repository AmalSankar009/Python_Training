def high(text):
    return text.upper()
 
def low(text):
    return text.lower()
 
def txt(func):
    str = func("""My name is Amal""")
    print (str)
 
txt(high)
txt(low)