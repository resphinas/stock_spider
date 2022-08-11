
try:
    numerator = int(input("Enter the numerator: "))

    while True:
        denominator = int(input("Enter the denominator: "))
        if denominator==0:
            print("the denominator can not be number 0, please enter a valid number again ")
            continue
        break
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


"""
When will a ValueError occur?
if the string we enter not required the type requirements we have define, like int,float,double..  it needs numbers but not char 
When will a ZeroDivisionError occur?
if we divide a number by number of 0
Could you change the code to avoid the possibility of a ZeroDivisionError?
yes
If you could figure out the answer to question 3, then make this change now.

"""