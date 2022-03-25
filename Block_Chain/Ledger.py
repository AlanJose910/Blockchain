# Transaction Block
import pickle

from Transaction.transaction import tx
from Block_Chain.Block_chain import CBlock
from Digital_Signaature.Signature import *

class TxBlock (CBlock):
    def __init__(self, previousBlock):
        pass
    def addTx(self, Tx_in):
        pass
    def is_valid(self):
        return False


if __name__ == "__main__":
    pr1, pu1 = key_gen()
    pr2, pu2 = key_gen()
    pr3, pu3 = key_gen()

    Tx1 = tx()
    Tx1.add_input(pu1, 1)
    Tx1.add_output(pu2,1)
    Tx1.sign(pr1)

    print(Tx1.is_valid())

    message = b"Some text"
    sig = sign(message, pr1)

    savefile = open("save.dat", "wb")
    # pickle.dump(Tx1, savefile)
    savefile.close()

    loadfile = open("save.dat", "rb")
    newTx = pickle.load(loadfile)

    print(newTx.is_valid())












