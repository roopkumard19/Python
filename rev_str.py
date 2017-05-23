def reverse(string):
	if len(string) <= 1:
		return string
	else:
		return reverse(string[1:]) + string[0]

def reverse_word(text):
	text = reverse(text)
	text = text.split(" ")
	
	result = []
	
	for item in text:
		temp = reverse(item)
		result.append(temp)
	return result

if __name__ == '__main__':
	s = raw_input("Enter the string to be reversed: ")
	s = reverse_word(s)
	print s
