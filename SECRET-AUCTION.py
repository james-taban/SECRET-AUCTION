from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
new_dictionary = {}
checker = 0
winner = ""
should_continue = True
def auction_dictionary(name, bid):
  new_dictionary[str(name)] = bid

print(logo)
print("Welcome to the blind auction")


while should_continue:
 name =input("What is your name? ")
 bid = int(input("what is your bid? $"))
 auction_dictionary(name,bid)
 choice = input("Do you want to continue? Type Yes or No ").lower()
 if choice == "yes":
   clear()
 elif choice == "no":
   should_continue = False

for key in new_dictionary:
  score = new_dictionary[key]
  if score > checker:
    checker = score
    winner = key

print(f"The highest bidder is {winner} with a bid of ${checker}.")
    