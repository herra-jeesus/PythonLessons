"""
Ülesanne 20 - Binary Search Trees
Juhend: https://courses.cs.ttu.ee/w/images/e/e7/2014_Loeng_21_-_Binary_tree.pdf
"""
__author__ = "Borka Martin Orlov"
__email__ = "borka.orlov@gmail.com"

from bst import *

def read_words(fail):
    """
    Loe sõnad failist
    """
    file_contents = fail.read()
    word = ""

    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            word += char
        else:
            if word != "":
                yield word
                word = ""

def main():
    try:
        fail = open("hound.txt", encoding="utf8")
    except Exception as e:
        print("Error occured when opening fail:", e)
    else:
        words = read_words(fail)
        tree = Tree(next(words))
        [tree.add(Tree(word)) for word in words]
        node, dist = tree.search("was")
        if node:
            node.printTree(1)
            print('Distance from root:', dist)

        print(tree.maxDepth())
        
        outputFile = open("result.txt", "w", encoding="utf8")
        tree.printToFile(outputFile)
        outputFile.close()
    finally:
        fail.close()

if __name__ == "__main__":
    main()