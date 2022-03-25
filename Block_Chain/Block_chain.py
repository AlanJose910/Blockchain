from Hashing import hash_fun

class someclass:
    string = None
    num = 123

    def __init__(self, mystring):
        self.string = mystring

    def __repr__(self):
        return self.string + str(self.num)


class CBlock:
    data = None
    previousHash = None
    previousblock = None

    def __init__(self, data, previousblock):
        self.data = data
        self.previousblock = previousblock
        if self.previousblock != None:

            self.previousHash = previousblock.computeHash()



    def computeHash(self):
        return hash_fun(bytes(str(self.data),'utf8'),bytes(str(self.previousHash),'utf8'))

if __name__ == '__main__':
    root = CBlock('I am robot', None)
    B1 = CBlock('I am a child', root)
    B2 = CBlock('I am B1s Brother', root)
    B3 = CBlock(12344, B1)
    B4 = CBlock(someclass('Hi there'), B3)
    B5 = CBlock("Top block", B4)

    for b in [B1, B2, B3, B4, B5]:
        if b.previousblock.computeHash() == b.previousHash:
            print("Sucess! Hash is good")
    else:
        print("Error! Hash is not good")


## Data Tampering ##

    B3.data = 12345
    if B4.previousblock.computeHash() == B4.previousHash:
        print ("Error! Could not detect data tampering")
    else:
        print("Data is tampered")

    B4.data.num = 44444
    if B5.previousblock.computeHash() == B5.previousHash:
        print ("Error! Could not detect data tampering")
    else:
        print("Data is tampered")







