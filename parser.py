# this should be renamed tokenizer

import enchant

englishDictionary = enchant.Dict("en_US")

wordy = "mas"
wordyRoot = ""

if wordy[-3:] == "ing":
	wordyStrip = wordy[:-3]
	wordyCheck = englishDictionary.check(wordyStrip)
	print wordyStrip, wordyCheck

	if not wordyCheck:
		if wordyStrip[-2:-1] == wordyStrip[-1:]:
			wordyFall = wordyStrip[:-1]
			wordyFallCheck = englishDictionary.check(wordyFall)
			print wordyFall, wordyFallCheck
			wordyRoot = wordyFallCheck
		elif englishDictionary.check(wordyStrip + "e"):
			print wordyStrip + "e"
			wordyRoot = wordyStrip + "e"

elif wordy[-1:] == "s" and len(wordy) > 3:
	print wordy[:-1]
	if englishDictionary.check(wordy[:-1]):
		print "ur mum"








terminals = {'.': '<PERIOD>', '!': '<EXCLAMATION_POINT>', '?': '<QUESTION_MARK>'}

nonterms = {':': ['<COLON>', 18], ';': ['<SEMI_COLON>', 19], ',': ['<COMMA>', 20], '@': '<AT_SIGN>', '#': '<POUND_SIGN>', '%': '<PERCENT_SIGN>',
			'$': '<DOLLAR_SIGN>', '^': '<CARET>', '&': '<AMPERSAND>', '*': '<ASTERISK>', '(': '<STARTING_PAREN>', ')': '<ENDING_PAREN>', 
			'\\': 'BACK_SLASH', '/': 'FORWARD_SLASH', '{': 'LEFT_CURLY_BRACE', '}': 'RIGHT_CURLY_BRACE', '<': 'LESS_THAN', 
			'>': '<GREATER_THAN>', '-': '<MINUS>', '_': '<UNDERSCORE>', '+': '<PLUS>', '=': '<EQUALS>', '[': '<LEFT_SQUARE_BRACKET>', 
			']': '<RIGHT_SQUARE_BRACKET>', '|': '<LINE_SEPERATOR>'}

whitespace = {'	': '<TAB>', ' ': '<SPACE>', '\n': '<NEWLINE>'}

singlecharwords = ['a', 'i', 'A', 'I']

word = ""


# this needs to be added into a string and then detected afterwards when a space hits
# IF a letter comes aferwards then we need to add it to the word based on what letter we think it is
# 	unless its an f, then we assume they are talking about a float var until we see another letter
# IF a period comes along we need to assume that it is a period or a decimal point and interpolate afterwards
number = ""

print

for char in "	This is a cool string, and I made it all by myself.?!":

	if char.isalpha():
		if char.isupper():
			print "<LETTER><CAPITAL>"
		else:
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
		print "<WHITE_SPACE>" + whitespace[char]

	elif char in terminals:
		if len(word) > 0 and englishDictionary.check(word):
			if len(word) == 1 and word not in singlecharwords:
				pass
			else:
				print "Found word: " + word
		word = ""
		print "<TERMINAL>" + terminals[char]

	elif char in nonterms:
		print "<NON-TERMINAL>", nonterms[char][0]

	else:
		nonterms[char] = char
		print "<UNRECOGNIZED> \'" + nonterms[char] + "\'"
		word = ""

print