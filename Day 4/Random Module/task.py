import random
import mymodule

#  num = random.randint(1,10)
# num = random.random()
#
# print(f"Random number: {num}")
# print(f"Favourite number: {mymodule.myFavouriteNumber}")

# heads or tails

randomVal = random.randint(0, 1)

if randomVal%2==0:
    print("Heads")
else:
    print("Tails")
