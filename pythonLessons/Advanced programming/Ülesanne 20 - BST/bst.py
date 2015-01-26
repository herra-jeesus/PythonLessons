class Tree:
    def __init__(self, data, count = 1, left = None, right = None):
        self.data = data
        self.count = count
        self.left = left
        self.right = right

    def add(self, node):
        """
        Node add
        """
        if node.data == self.data:
            self.count += 1
            return

        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)

    def maxDepth(self):
        """
        Tagastab maksimaalse sügavusega elemendi sügavuse.
        """
        if self.left is None and self.right is None:
            return 0

        if self.left is None:
            lDepth = 0
        else:
            lDepth = self.left.maxDepth()

        if self.right is None:
            rDepth = 0
        else:
            rDepth = self.right.maxDepth()

        return max(lDepth, rDepth) + 1

    def minValue(self):
        """
        Tagastab kõige väiksema väärtusega elemendi
        """
        if self.left is None: return self
        return self.left.minValue()

    def printTree(self, depth = None):
        """
        Prindib puu elemendid välja rekursiivselt. Tulemus peaks olema sorteeritud sõnastik. 
        """
        if depth is not None:
            if depth == 0: return
            depth -= 1

        if self.left is not None:
            self.left.printTree(depth)
        print(self.data, ":", self.count)
        if self.right is not None:
            self.right.printTree(depth)

    def printToFile(self, file):
        """
        Puu faili
        """
        if self.left is not None:
            self.left.printToFile(file)
        file.write(self.data + " : " + str(self.count) + "\n")
        if self.right is not None:
            self.right.printToFile(file)

    def search(self, word, _dist = 0):
        """
        tagastab node'i, mille otsitav sõna sisaldub, kauguse juurelemendist. Lisaks
        tagastab sõnade arvu (mitu korda seda sõna tekstis esines). Kui sõna ei leidu, tuleks vastav
        teade anda.
        """
        if word == self.data:
            return (self, _dist)
        else:
            if self.left is None and self.right is None:
                return (False, None)
            if word < self.data:
                _dist += 1
                return self.left.search(word, _dist)
            else:
                _dist += 1
                return self.right.search(word, _dist)

if __name__ == "__main__":
    pass