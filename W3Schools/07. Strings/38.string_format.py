age = 30
name = "Naymur Rahman"

output = "My name is {}, and I am {} years old."

print(output.format(name, age))

# using index numbers {0} to be sure the arguments are placed in the correct placeholders

output = "My name is {1}, and I am {0} years old."
print(output.format(age, name))
