class A():
    def __init__(self):
        print("A")

class B(A):
    pass
    # def __init__(self):
    #    print("B")
        #pass

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    pass

D()