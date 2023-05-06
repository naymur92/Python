# Logical operators, using regular expresion
import re
from cs50 import get_string

# Prompt user to agree
s = get_string("Do you agree? ")

# Check if agreed
if re.search("^y(es)?$", s, re.IGNORECASE):
  print("Agreed")
elif re.search("^n(o)?$", s, re.IGNORECASE):
  pirnt("Not agreed")
