"""
Ülesanne 11 - RegEx
Juhend: https://courses.cs.ttu.ee/w/images/0/07/2014_Loeng_11_-_Regular_expressions.pdf

Ülesanded lehelt https://cs.uwaterloo.ca/~dtompkin/teaching/08a/lab7/
1-5, 9-12, valida 3 13-19 seast.
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

def main():
	excercise_1 = '^[10]*'
	excercise_2 = '^[10]*0'
	excercise_3 = '^(00|01|10|11)*$'
	excercise_4 = '^[01]*(0110|1001)[01]*$'
	excercise_5 = '^([01]*)((0110[01]*1001)|(1001[01]*0110)|(011001)|(100110))([01]*)$'

	excercise_9 = '^pick[\s-]{0,1}(up)\s(truck)$'
	excercise_10 = '([A-Za-z0-9,]*\s){2,3}[A-Za-z0-9]*[.!?]?$'
	excercise_11 = '^(cat)\s([a-zA-Z]*\s){0,2}(hat)$'
	excercise_12 = '([01]?[0-9]|2[0-3]):[0-5][0-9]'

	excercise_13 = '[ACGT]*(ATG)([ACGT]{3}){1,}(TAA|TAG|TGA)[ACGT]*'
	excercise_16 = '(1|01*0)+'
	excercise_17 = '^0?(10)*1?$'

if __name__ == '__main__':
	main()