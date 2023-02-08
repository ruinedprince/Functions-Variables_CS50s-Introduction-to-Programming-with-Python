def main():
    z = int(input("(What's z?"))
    print("z squared is", square(z))

def square(n):
    return pow(n, 2)               # Pow is a short for Power. It's used to calculate square values, been the number after comma the times that the variable will be mutiplied.
x = float(input("What's x? "))     
y = float(input("What's z? "))     # Adding the x and y's values as float values. Int is a function. Here i'm nesting function and argument.

z = round(x + y)                   # Rounding the float value to the nearest int value.

print (f"{z:,}")                   # Printing the values as int. ":," is used to separate the numeral places correctly and automatically.

z = round(x / y, 2)                # Round is used to choose the quantity of digits of decimals values.

print(f"{z:.2f}")                  # The ".2f" method works like the ":," one, but without use round method, but the f-string form.

# using return #
main()