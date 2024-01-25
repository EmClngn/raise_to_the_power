# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# pseudo code

# user input for base and exponent numbers
input_base = int(input("What is your desired base number?: "))
input_exp = int(input(f"Raise {input_base} to the power of what?: "))
products = []
# make a function and inside it use for loop to raise the base to the power of the exp
# make an empty list for append
# call the function
def exponent(base, exp):
    for _ in range(exp + 1):
        base *= exp
        products.append(base)
    print(products[-1])

exponent(input_base, input_exp)

