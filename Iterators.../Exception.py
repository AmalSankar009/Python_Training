try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    print("It is an even number")
finally:
    print("Done")

#OUTPUT

# Enter a number: 5
# Not an even number!
# Done    

# Enter a number: 4
# It is an even number
# Done