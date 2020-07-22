bits = [10, 1, 2] # edit this
down = [11] # edit this
hits = 0
for number in bits:
    if number in down:
        hits += 1

nothits = 0
for number in bits:
    if number not in down:
        nothits += 1
        
print("You hits : ", hits)
print("You can't hits : ",nothits)
