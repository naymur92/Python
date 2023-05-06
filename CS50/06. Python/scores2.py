def main():
  scores = []
  for i in range(3):
    score = get_score()
    scores += [score]

  average = sum(scores) / len(scores)
  print(f"Average: {average}")


def get_score():
  while True:
    try:
      n = int(input("Score: "))

      if n > 0:
        return n
    except ValueError:
      print("Not an integer!")


main()
