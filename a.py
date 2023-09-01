import random
accumulator = 0
running = 0
for i in range(1000):
    for ii in range(7):
        if random.randint(0,100) <= 65:
            accumulator = accumulator + 1
    if accumulator >= 4:
        running += 1
        accumulator = 0
print(running)
