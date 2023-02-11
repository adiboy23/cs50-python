# Ask user for their name
name = input("What's your name? " )

# Removes white spaces before and after the string
name = name.strip()

# Capitalize the users input but only the first name
name = name.capitalize()

# The below method capitalizes both firt and last name
name = name.title()

print(f"Hello, {name}")
