import random
def number_guessing_game():
  secret = random.randint(1, 100)
  attempts = 7
  print("Guess the number (1-100)")
  print("You have 7 attempts")
  while attempts > 0:
      guess = int(input("Your guess: "))

      if guess == secret:
          print("You win!")
          break
      elif guess < secret:
          print("Too low")
      else:
          print("Too high")

      attempts = attempts - 1
  if attempts == 0:
      print("Game over! The number was", secret)
number_guessing_game()