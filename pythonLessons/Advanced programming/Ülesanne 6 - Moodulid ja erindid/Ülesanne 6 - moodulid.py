"""
Kuues kodune töö
Moodulid ja erindid
Juhend: https://courses.cs.ttu.ee/w/images/5/5d/ITI0140_Loeng_6_-_Moodulid_ja_erindid.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

import text_processing

def main():
	# Ava fail
	try:
		tekst = open('The Hound of the Baskervilles.txt', 'r')
	except:
		print('Ilmnes viga')
		exit()
	# Tekita sõnade list
	word_list  = text_processing.process_file(tekst)
	# Loe korduvad sõnad kokku
	dct = text_processing.count_words(word_list)
	# Sordi sõnastik
	sorted_dct = text_processing.find_top_words(dct, 7)
	# Väljasta tulemus
	text_processing.print_top_words(sorted_dct, 'ex6_output.txt')
	# Sulge fail
	tekst.close()

if __name__ == '__main__':
	main()