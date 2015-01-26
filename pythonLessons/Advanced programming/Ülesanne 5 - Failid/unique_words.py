"""
Modules for exercise 5
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

def count_words(file_name, word_array):
	"""
	Loeb kokku sõnade arvu ja unikaalsete sõnade arvu.
	Lisab unikaalsed sõnad listi
	"""
	word_count = 0
	book = open(file_name, 'r')
	for line in book:
		line = line.split()
		for word in line:
			if word.isalpha():
				word_count = word_count + 1 
				if word not in word_array:
					word_array.append(word)
	print('Tekstis', file_name, 'on kokku', word_count, 'sona.' )
	
	length = len(word_array)
	print('Kokku on', length, 'unikaalset sona')

	return length
	
def compare_words(unique_1, unique_2):
	"""
	Leiab mitu unikaalset sõna on esimeses listis, mida teises pole
	"""
	uniques = 0
	for word in unique_1:
		if word not in unique_2:
			uniques = uniques + 1
	print ('Tekstis on ', uniques, 'sona mida teises pole.')

def words_in_both(unique_1, unique_2):
	uniques = 0
	for word in unique_1:
		if word in unique_2:
			uniques = uniques + 1
	print (uniques, 'sona esineb molemas tekstis')