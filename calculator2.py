# Take users input 
x = float(input("What's x? "))
y = float(input("What's y? "))

# round off the sum of x and y
z= round(x + y)

# print the sum of float x and y. We are using the f-string here to format the output and add commas in the output.
print(f"{z:,}")

