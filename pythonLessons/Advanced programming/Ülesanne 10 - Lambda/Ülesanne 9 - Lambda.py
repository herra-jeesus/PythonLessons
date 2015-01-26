"""
Ülesanne 9 - Lambda
Juhend: https://courses.cs.ttu.ee/w/images/5/54/2014_Loeng_10_-_Lambda%2C_comprehensions_and_generator.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

def generator(filename):
    text_file = open(filename, 'r')

    for line in text_file:
        word = ''
        for char in line:
            if char.isalpha():
                word = word + char
            elif char in [' ', '!', '?', ',', '.', ':']:
                yield word
                word = ''
    text_file.close()


def main():
    list_of_words = [x for x in generator('HoundOfTheBaskervilles.txt')][3:400:4]
    print('Sõnade arv listis: ', len(list_of_words))
    average = sum(map(len, list_of_words))/len(list_of_words)
    print('Sõnade keskmine pikkus', average)
    list_of_words = list(filter(lambda x: len(x) > average, list_of_words))
    print(list(filter(lambda x: x.capitalize(), list_of_words)))

if __name__ == '__main__':
    main()
