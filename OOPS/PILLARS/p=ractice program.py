class x:
     def demo(self,name,age):
        self.name=name
        self.age=age
    def __init__(self):
        print({self.name})
        print({self.age})
a=x("vidhi",21)
a.__init__()

