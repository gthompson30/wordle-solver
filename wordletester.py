from math import floor

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

def assess_move(set_of_answers, move):
	dist = {}
	chars = '012'
	for first in chars:
		for second in chars:
			for third in chars:
				for fourth in chars:
					for fifth in chars:
						dist[first + second + third + fourth + fifth] = []
	for next_guess in set_of_answers:
		result = assess_guess(move, next_guess)
		dist[result].append(next_guess)
	return dist

total = 0

for index, correct in enumerate(answers):
	set_of_answers = answers
	result = assess_guess('salet', correct)
	set_of_answers = assess_move(set_of_answers, 'salet')[result]
	num_guesses = 2
	print('salet ' + result)
	
	while len(set_of_answers) > 1:
		rankings = {}
	
		for word in allowed:
			#print(f'Testing {word}...')
			dist = assess_move(set_of_answers, word)
			with_some = len([i for i in dist if len(dist[i]) >= 1])
			rankings[word] = len(allowed) / with_some
	
		rankings = sorted(rankings.items(), key=lambda x: x[1])
		result = assess_guess(rankings[0][0], correct)
		set_of_answers = assess_move(set_of_answers, rankings[0][0])[result]
		num_guesses += 1
		print(f'{rankings[0][0]} {result}')

	total += num_guesses
	print(f'{correct} 22222')
	print()
	#if answers:
		#print(f'Solved {correct} in {num_guesses} guesses       |  Average: ' + '{:.2f}'.format(total / (index + 1)) + f'  | {index + 1}/{len(answers)}')
	#else:
		#print('Could not find an answer!')
