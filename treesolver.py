import json

with open('data/tree.json', 'r') as f:
	data = json.load(f)

while len(data[1]) > 0:
	print(f"Enter \"{data[0]}\"")
	a = input("Result: ")
	data = data[1][a]

print(f"Answer: \"{data[0]}\"")
