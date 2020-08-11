
import math

probs = [0.0175, 0.047585, 0.351609, 0.010618, 0.003906, 0.351609, 0.213262, 0.003906]

entropy = 0
print("sum probs:", sum(probs))
for p in probs:
    entropy += (-1*p)* (math.log(p))

print("en:", entropy)