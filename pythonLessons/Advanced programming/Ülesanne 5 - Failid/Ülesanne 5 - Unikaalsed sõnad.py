"""
Tekstitöötluse ülesande alus on kaks A. C. Doyle'i raamatut, mis on vabalt kättesaadavad Project
Gutenberg kaudu:
1)A Study in Scarlet (.txt)
2)The Hound of the Baskervilles (.txt)

Tekstid on vaja jaotada sõnadeks. Sõnaks loeme antud juhul kõik järjest asetsevad tähed, mille kohta Pythoni isalpha()
funktsioon vastab tõeselt. Sõnade ümber asetsevad muud sümbolid. Sõnadeks jaotamine ei peaks olema tõstutundlik.

Leida:
1)kui palju on sõnu kokku tekstis 1
2)kui palju on sõnu kokku tekstis 2
3)kui palju on unikaalseid sõnu tekstis 1
4)kui palju on unikaalseid sõnu tekstis 2
5)kui palju on unikaalseid sõnu tekstis 1 ja tekstis 2 kokku
6)kui palju on unikaalseid sõnu tekstis 1, mida tekstis 2 pole
7)kui palju on unikaalseid sõnu tekstis 2, mida tekstis 1 pole
8)kui palju on unikaalseid sõnu, mis esinevad mõlemas tekstis


"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

import unique_words

# Unikaalsed sõnad mõlema teksti kohta
unique_words_scarlet      = []
unique_words_baskervilles = []

def main():
	global unique_words_baskervilles, unique_words_scarlet

	# Ülesanded 1-4
	# Leida sõnade kogusumma ja unikaalsete sõnade arv mõlemas tekstis ja lisab nad listi
	# Tagastab unikaalsete sõnade arvu järgneva ülesande jaoks
	wordcount_1 = unique_words.count_words('A Study in Scarlet.txt', unique_words_scarlet)
	wordcount_2 = unique_words.count_words('The Hound of the Baskervilles.txt', unique_words_baskervilles)

	# Ülesanne 5
	# Unikaalseid sõnu kahe teksti peale kokku 
	print('Unikaalseid sonu on kahe teksti peale', wordcount_1 + wordcount_2)

	# Ülesanded 6-7
	# Unikaalseid sõnu mida teises tekstis pole
	print('A Study in Scarlet:', end=' ')
	unique_words.compare_words(unique_words_scarlet, unique_words_baskervilles)
	print('The Hound of the Baskervilles:', end=' ')
	unique_words.compare_words(unique_words_baskervilles, unique_words_scarlet)

	# Ülesanne 8
	# Unikaalsete sõnad mis esinevad mõlemas tekstis
	unique_words.words_in_both(unique_words_scarlet, unique_words_baskervilles)
	
# Beginning
if __name__ == '__main__':
	main()