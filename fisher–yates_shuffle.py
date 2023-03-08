import random

target = ['A', 'B', 'C', 'D']
target_copy = ['', '', '', '']
randomNumbers = []

n = (len(target) - 1)
i = 0
while True:
    a = random.randint(0, n)
    if(a in randomNumbers):
        continue
    else:
        target_copy.pop(a)
        target_copy.insert(a, target[i])
        print("the index is:", a)
        randomNumbers.append(a)
        i += 1
        print(target_copy)

    if(target[0] in target_copy and target[1] in target_copy and target[2] in target_copy and target[3] in target_copy):
        break
