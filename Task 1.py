# This for loop will print your name 10 times.
for i in range(10):
    print("Dany")

name = input("What is your name? ")
for i in range(1000):
    print(" Hello," + name)


# Ask for a number from the user
number = int(input("Enter a number for the times table: "))

# Calculate and print the times table for the entered number up to 12
for i in range(1, 13):
    # Concatenation of strings and type casting of integer to string
    print(str(number) + " x " + str(i) + " = " + str(number * i))


    # Ask for a number from the user
number = int(input("Enter a number for the times table: "))

# Calculate and print the times table for the entered number up to 1000
for i in range(1, 1001):
    # Concatenation of strings and type casting of integer to string
    print(str(number) + " x " + str(i) + " = " + str(number * i))