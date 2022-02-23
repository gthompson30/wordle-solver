answers = open('data/answers.txt').readlines()
answers = [answer.replace('\n', '') for answer in answers]

allowed = open('data/allowed.txt').readlines()
allowed = [word.replace('\n', '') for word in allowed]

def assess_guess(guess, correct):
	out = []
	added = {k: 0 for k in [chr(i) for i in range(ord('a'), ord('z') + 1)]}
	for index, letter in enumerate(guess):
		if letter == correct[index]:
			out.append('2')
			added[letter] += 1
		elif letter in correct:
			out.append('X')
		else:
			out.append('0')
	for index, code in enumerate(out):
		if code == 'X':
			if added[guess[index]] < correct.count(guess[index]):
				out[index] = '1'
				added[guess[index]] += 1
			else:
				out[index] = '0'
	return ''.join(out)

def assess_move(move):
	dist = {}
	chars = '012'
	for first in chars:
		for second in chars:
			for third in chars:
				for fourth in chars:
					for fifth in chars:
						dist[first + second + third + fourth + fifth] = []
	for next_guess in answers:
		result = assess_guess(move, next_guess)
		dist[result].append(next_guess)
	return dist


print('Enter "SALET"')
result = input('Enter the result: ')
answers = assess_move('salet')[result]

while len(answers) > 1:
	rankings = {}

	for word in allowed:
		print(f'Testing {word}...')
		dist = assess_move(word)
		with_some = len([i for i in dist if len(dist[i]) >= 1])
		rankings[word] = len(allowed) / with_some

	rankings = sorted(rankings.items(), key=lambda x: x[1])

	for i in range(10):
		print(f'{i} : {rankings[i]}')
	print('\n...\n')
	for i in range(len(rankings) - 10, len(rankings)):
		print(f'{i} : {rankings[i]}')

	result = input('Result: ')
	answers = assess_move(rankings[0][0])[result]

if answers:
	print('The answer is: ' + answers[0])
else:
	print('Could not find an answer!')
