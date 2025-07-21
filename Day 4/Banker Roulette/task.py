import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
chosen = random.randint(0, len(friends)-1)

print("I choose: "+ friends[chosen])


# or you could have done: random.choice(friends)
