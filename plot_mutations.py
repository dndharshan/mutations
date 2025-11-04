import matplotlib.pyplot as plt
from collections import Counter

positions = []

with open("mutations.txt") as f:
    for line in f:
        if "Position" in line:
            pos = int(line.split()[1].strip(":"))
            positions.append(pos)

counts = Counter(positions)

plt.bar(counts.keys(), counts.values())
plt.xlabel("Genome Position")
plt.ylabel("Mutation Count")
plt.title("SARS-CoV-2 Mutation Frequency")
plt.show()
