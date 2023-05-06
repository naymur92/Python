from cs50 import get_string

people = {
    "Naymur": "+880-1737-036324",
    "Kamrul": "+880-1558-981652",
}
name = get_string("Name: ")

if name in people:
  print(f"Phone number: {people[name]}")
