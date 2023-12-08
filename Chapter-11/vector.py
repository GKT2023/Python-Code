class C2dvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def details(self):
        print(f"2d vector is: {self.i}i + {self.j}j")

class C3dvector(C2dvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k = k
    def details(self):
        super().details()
        print(f"3d vector is: {self.i}i + {self.j}j + {self.k}k")
    

c2 = C2dvector(1,3)
c3 = C3dvector(4,5,6)

c2.details()
c3.details()