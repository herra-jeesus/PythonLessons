"""
Ülesanne 9 - Simulatsioonid
Simulatsioonid
Juhend: https://courses.cs.ttu.ee/w/images/9/9a/ITI0140_-_2014_-_Loeng_9_Simuleerimine.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

import random, timeit as t, math, itertools

def gcd(a, b):
	"""
	Greatest common divisor
	Suurima ühisteguri leidmine
	"""
	while b:
		a, b = b, a%b
	return a

def method_1(n):
	"""
	Meetod 1 - (Jaagu idee)
	Ruudukulisele alusele "noolte loopimine"
	Vt Juhend lk 8
	"""
	global pi
	random.seed()
	h = 0

	for i in range(n):
		x = 2 * random.random() - 1
		y = 2 * random.random() - 1
		if x*x + y*y <= 1: h += 1

	pi = 4 * h / n
	return pi

def method_2(n):
	"""
	Meetod 2 - (Peetri idee)
	Tuleb võtta n juhuslikult valitud täisarvu. Tõenäosus, et nende seast igal kahel
	suvalisel numbril pole ühiseid tegureid (peale 1 muidugi), on 6 / π^2.
	Vt Juhend lk 9
	"""
	global pi
	random.seed()
	num = 0

	while num == 0:
		numbers = set()

		for i in range(n):
			numbers.add(random.randint(2, 100))

			combos = list(itertools.combinations(list(numbers), 2))
			num = 0

		for numbers in combos:
			if gcd(numbers[0], numbers[1]) == 1:
				num += 1

	pi = math.sqrt(6 / (num / len(combos)))
	return pi

def test(testnr, rangenr):
	"""
	Testide jooksutamiseks loodud funktsioon
	"""
	for i in range(1, rangenr):
		n = 2**i
		time = t.timeit("method_{0}({1})".format(testnr, n), "from __main__ import method_{0}".format(testnr), number = 1)
		accuracy = abs(math.pi - pi)
		if n < 10000:
			print("| {0} \t| {1} \t\t| {2:.8f} \t| {3:.4f} \t| {4:.8f}".format("method_{0}".format(testnr), n, pi, time, accuracy))
		else:
			print("| {0} \t| {1} \t| {2:.8f} \t| {3:.4f} \t| {4:.8f}".format("method_{0}".format(testnr), n, pi, time, accuracy))

	print()


def main():
	print("| algorithm \t| n \t\t| pi \t\t| time \t\t| accuracy")

	# Test both methods
	# test(method nr, range of n)
	test(1,15)
	test(2,15)

if __name__ == "__main__":
	pi = 0 # global pi variable
	main()