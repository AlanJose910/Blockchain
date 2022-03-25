##   Hashing Example   ##

from Hashing import hash_fun


if __name__ == '__main__':
    message1 = b"233"
    message2 = b"124"
    hashing1 = hash_fun(message1,message2)
    print(hashing1)

    #####Checking the similarity####

    message3 = b"234"
    hashing2 = hash_fun(message3,message2)
    print(hashing2)



