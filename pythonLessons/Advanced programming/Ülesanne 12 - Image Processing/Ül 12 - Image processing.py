"""
Ülesanne 12 - Image Processing
Juhend: https://courses.cs.ttu.ee/w/images/d/d4/2014_Loeng_12_-_Image_processing.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

from PIL import Image, ImageDraw

def get_word_list(filename):
	"""
	Genereerib antud failist sõnade järjendi
	"""
	file_pointer = open(filename, 'r')
	word_list = []

	for line in file_pointer:
		words = line.split()
		for word in words:
			if word.isalpha():
				word_list.append(word)
	return word_list

def pair_frequency(word_list):
	"""
	genereerib sisendiks antud sõnede järjendist (nt ['Tere', 'banaan', ...]) kahemõõtmelise
	tähepaaride esinemissageduse maatriksi (nt 'te'*1, 'er'*1, 're'*1, 'ba'*1, 'an'*2, 'na'*1, 'aa'*1)
	"""
	pairs = {}
	for word in word_list:
		for index, char in enumerate(word):
			if index != len(word) - 1:
				pair = char + word[index + 1]
				if pair in pairs:
					pairs[pair] = pairs[pair] + 1
				else:
					pairs[pair] = 1
	return pairs

def create_heat_map(word_matrix):
	"""
	genereerib kahemõõtmelisest maatriksist soojuskaardi.
	Kasuta loodud funktsioone andes sisendiks sõned
	Baskerville'ide failist.
	"""
	return 0



def main():
	word_list = get_word_list('The Hound of the Baskervilles.txt')
	word_matrix = pair_frequency(word_list)
	print(word_matrix)
	#create_heat_map(word_matrix)

if __name__ == '__main__':
	main()