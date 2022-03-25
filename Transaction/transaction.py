# Transactions
import Digital_Signaature.Signature
from Digital_Signaature.Signature import *


class tx:
    inputs = None
    outputs = None
    signatures = None
    req_sig = None

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.signatures = []
        self.req_sig = []

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))

    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))

    def add_reqd(self, addr):
        self.req_sig.append(addr)

    def sign(self, private):
        message = self.__gather()
        sign1 = Digital_Signaature.Signature.sign(message, private)
        self.signatures.append(sign1)

    def is_valid(self):
        total_inn = 0
        total_out = 0
        message = self.__gather()
        #print (self.inputs)
        #print(message)
        #print(self.signatures)
        for adress, amount in self.inputs:
            found = False
            for s in self.signatures:
                if verify(message, s, adress):
                    found = True
            if not found:
                return False
            if amount < 0:
                return False
            total_inn = total_inn + amount
        for adress in self.req_sig:
            #print(adress)
            #print(message)
            #print(self.signatures)
            found = False
            for s in self.signatures:
                if verify(message, s, adress):
                    #print(True)
                    found = True
            if not found:
                #print(False)
                return False
        for adress,amount in self.outputs:
            if amount < 0:
                return False
            total_out = total_out + amount
        if total_out > total_inn:
            return False
        return True

    def __gather(self):
        data = []
        data.append(self.inputs)
        data.append(self.outputs)
        data.append(self.req_sig)
        return data


if __name__ == "__main__":
    pr1, pu1 = key_gen()
    pr2, pu2 = key_gen()
    pr3, pu3 = key_gen()
    pr4, pu4 = key_gen()
    print(pu4)

    Tx1 = tx()
    Tx1.add_input(pu1, 1)
    Tx1.add_output(pu2, 1)
    Tx1.sign(pr1)

    Tx2 = tx()
    Tx2.add_input(pu1, 2)
    Tx2.add_output(pu2, 1)
    Tx2.add_output(pu3, 1)
    Tx2.sign(pr1)

    Tx3 = tx()
    Tx3.add_input(pu3, 1.2)
    Tx3.add_output(pu1, 1.1)
    Tx3.add_reqd(pu4)
    Tx3.sign(pr3)
    Tx3.sign(pr4)

    for t in [Tx1, Tx2, Tx3]:
        if t.is_valid():
            print("Sucess! Transaction is valid")
        else:
            print("Error! Transaction is invalid")

    # wrong signatures
    Tx4 = tx()
    Tx4.add_input(pu2, 1)
    Tx4.add_output(pu1, 1)
    Tx4.sign(pr1)

    # Escrow Transaction not signed by the arbiter
    Tx5 = tx()
    Tx5.add_input(pu3, 1.2)
    Tx5.add_output(pu1, 1.1)
    Tx5.add_reqd(pu4)
    Tx5.sign(pr3)

    # Two input address, signed by one

    Tx6 = tx()
    Tx6.add_input(pu3, 1)
    Tx6.add_input(pu4, 0.1)
    Tx6.add_output(pu1, 1.1)
    Tx6.sign(pr3)

    # Output exceed the inputs

    Tx7 = tx()
    Tx7.add_input(pu4, 1.2)
    Tx7.add_output(pu1, 1)
    Tx7.add_output(pu2, 2)
    Tx7.sign(pr4)

    # Negative Values

    Tx8 = tx()
    Tx8.add_input(pu2, -1)
    Tx8.add_output(pu1, -1)
    Tx8.sign(pr2)

    # Modified Transaction

    Tx9 = tx()
    Tx9.add_input(pu1, 1)
    Tx9.add_output(pu2, 1)
    Tx9.sign(pr1)
    Tx9.outputs[0] = (pu3,1)

    for t in [Tx4, Tx5, Tx6, Tx7, Tx8, Tx9]:
        if t.is_valid():
            print("Error! Bad transaction is valid")
        else:
            print("Sucess! Bad Transaction is invalid")