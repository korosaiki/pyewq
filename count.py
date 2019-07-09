class Count:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
#这下面的内容不能被调用到
if __name__ == '__main__':
    a = Count(3,5)
    print(a.add())