import enchant

englishDictionary = enchant.Dict("en_US")

terminals = {'.': '<PERIOD>', '!': '<EXCLAMATION_POINT>', '?': 'QUESTION_MARK'}
nonterms = {'$': '<DOLLAR_SIGN>'}
whitespace = {'	': '<TAB>', ' ': '<SPACE>', '\n': '<NEWLINE>'}
singlecharwords = ['a', 'i']

word = ""

print

for char in "this	is a c00l \nstring $.!":

	if char.isalpha():
		print "<LETTER>"
		word += char

	elif char.isdigit():
		print "<DIGIT>"
		word = ""

	elif char in whitespace:
		if len(word) > 0 and englishDictionary.check(word):
			if len(word) == 1 and word not in singlecharwords:
				pass
			else:
				print "Found word: " + word
		word = ""
		print whitespace[char]

	elif char in terminals:
		if len(word) > 0 and englishDictionary.check(word):
			if len(word) == 1 and word not in singlecharwords:
				pass
			else:
				print "Found word: " + word
		word = ""
		print "<TERMINAL>" + terminals[char]
		print "End sentence"

	elif char in nonterms:
		print nonterms[char]

	else:
		nonterms[char] = char
		print "<UNRECOGNIZED> \'" + nonterms[char] + "\'"
		word = ""

print