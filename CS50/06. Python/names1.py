import sys

names = ["Naymur", "Kamrul", "Rana", "Jamil", "Sohag"]

name = input("Name: ")

if name in names:
  print("Found")
  sys.exit(0)

print("Not found")
sys.exit(1)
