"""
Kuues kodune töö
Moodulid ja erindid
Juhend: https://courses.cs.ttu.ee/w/images/5/5d/ITI0140_Loeng_6_-_Moodulid_ja_erindid.pdf
MOODUL
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

def process_file(fail):
	"""
	Võtab argumendiks avatud faili ja tagastab teksti sõnadeks jaotamise tulemusena
	tekkiva järjendi (st kõik sõnad tekstist nende leidmise järjekorras, sh kordused)
	"""
	word_list = []
	for line in fail:
		line = line.split()
		for word in line:
			if word.isalpha():
				word_list.append(word)

	return word_list

def count_words(list):
	"""
	võtab argumendiks sõnade järjendi ja tagastab sõnastiku, kus võti on sõna ja
	väärtus on selle sõna esinemiste arv
	"""
	dct = {}
	for word in list:
		if word in dct:
			dct[word] = dct[word] + 1
		else:
			dct[word] = 1
	return dct

def getKey(item):
	return item[1]

def find_top_words(dct, n):
	"""
	võtab argumendiks count_words() tagastatava sõnastiku ja tagastab
	sõnastiku, kus võti on sõna pikkus ja väärtus on n sagedasemalt esinenud sõna vastava pikkusega ja
	esinemiste arvuga (st omakorda kuni n pikkused järjendid ennikutest või sõnastikud)
	"""
	dct = sorted(dct.items(), key=lambda dct: dct[1])
	sorted_dct = {}
	for word in dct:
		if word[1] > n:
			sorted_dct.setdefault(word[1], []).append(word[0])

	sorted_dct = sorted(sorted_dct.items(), key=lambda sorted_dct: sorted_dct[0], reverse=True)
	return sorted_dct

def print_top_words(dct, filename):
	"""
	võtab vastu find_top_words() tagastatava sõnastiku ja trükib
	tulemustest viisakalt vormindatud tabeli faili, sõnade pikkuse järgi kasvavalt, sõnade esinemise sageduse
	järgi kahanevalt, sama sageduse korral tähestiku järjekorras.
	"""
	fail = open(filename, 'w')
	string = '|{0:6}|{1:12}|{2:7}|\n'.format('Count', 'Word', 'Length')
	fail.write(string)
	for words in dct:
		word_list = sorted(words[1], key=str.lower)
		for word in word_list:
			#fail.write(str(words[0])+ '|'+ word+ '|'+ str(len(word)) + '\n')
			string = '|{0:6}|{1:12}|{2:7}|\n'.format(words[0], word, len(word))
			fail.write(string)

	fail.close()

	return 0