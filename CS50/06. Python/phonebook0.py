import csv

# Open csv file
file = open("phonebook.csv", 'a')

# Get name and number
name = input("Name: ")
number = input("Number: ")

# Print to file
writer = csv.writer(file)
writer.writerow([name, number])

# Close file
file.close()