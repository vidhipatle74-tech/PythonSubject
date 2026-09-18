# Outside Modification in class variable using getter, setter and deleter:==>>
"""
class Bank:
    def __init__(self,name,account_number,balance):
        self.name=name   #public
        self._account_number=account_number   #protected
        self.__balance=balance    #private

    def Getter(self):
        print(getattr(self,"name","name is deleted"),
                getattr(self,"_account_number","account_number is deleted"),   #to see the value is deleted or not , internally it was deleted
                                                                                                                    #but if we want to see then we can go  for getattr methof or
                                                                                                                    #inbuild function
              
                getattr(self,"_Bank__balance","balance is deleted"))

    def Setter(self,name,account_number,balance):
        self.name=name
        self._account_number=account_number
        self.__balance=balance

    def Deleter(self):
        del self.__balance

b=Bank("vidhi",1234567890,8000)
b.Getter()
b.Setter("Kiran",1234567890,6000)
b.Getter()
b.Deleter()
b.Getter()
"""
#o/p--> vidhi 1234567890 8000   --> first one 
#           Kiran 1234567890 6000   ---> updated one


class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def data(self):
        return getattr(self,"name","the name is deleted"),getattr(self,"age","the age is deleted")

    @data.setter
    def data(self,new_name,new_age):
         self.new_name,self.new_age

    @data.deleter
    def data(self):
        del self.name

e=Employee('xyz',23)
print(e.data)
e.data=('ABC',21)
print(e.data)
del e.data
print(e.data)

        
