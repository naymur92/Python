import csv

# Get name and number
name = input("Name: ")
number = input("Number: ")

# Open csv file
with open("phonebook.csv", 'a') as file:
  writer = csv.writer(file)
  writer.writerow([name, number])
