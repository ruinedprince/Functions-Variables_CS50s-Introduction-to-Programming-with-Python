def main():
    name2 = input("What's your name? ")
    hello(name2)
def hello(to="world"):
    print("hello,",to)                                      # Def is a shor for define. Is used to define a custom function for the code.You can also use parameters to manipulate values of variables
# Ask user for their name #
# Remove whitespace from name str and capitalize user's name #

name = input("What's your name?")                          # 'name' is the variable's name

# Split user's name into first name and last name #
first, last = name.split(" ")
name = name.strip().title()
# Say hello to user #
print ("Hello,", name, sep="???")                       # 'print' is the funcion, and the content between parentheses is the argument will work on. 'sep="???"' argument override the defaul ' ' value and makes the print funcion print '???' instead a ' ' when the arguments are separated.

print ("Hello, ", end="")                               # 'end=""' argument override the default "\n" value and makes the print function doesn't break to a new blank line at the end of the text.

print (name)                                            # Returns the name's funcion.

print (f"Hello, {first}")
print (f"Hello, {last}")                                # f-strings.

# using defined functions #
main()