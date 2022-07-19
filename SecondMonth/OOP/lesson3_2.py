class A:

    def get_text(self):
        pass


class B:
    def get_text_2(self):
        pass


class C(A, B):
    pass


d1 = C()
print(C.mro())
