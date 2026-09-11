"""class grandpa:

    def agriland(self):
        print('land')

class father(grandpa):
    def property(self):
        print('home')

class child(father):
    def bike(self):
        print('bike')

c=child()
c.bike()
c.property()
c.agriland()
"""

#o/p--> bike
#           home
#         land

#BY USING SUPER FUNCTION-=====>>>
"""
class dad:
    
    def money(self):
        print('1CR')
        
class child1(dad):
    
    def money(self):
        super().money()
        print('50Lakh')

class child2(child1):

    def money(self):
        super().money()
        print('25Lakh')

c=child2()
c.money()
"""    
#o/p--> 1CR
#           50Lakh
#           25Lakh

#BY USING CLASS NAME WE HAVE TO EXPLICITELY PASS OBJECT===>>>
"""
class dad:
    
    def money(self):
        print('1CR')
        
class child1(dad):
    
    def money(self):
        dad.money(self)
        print('50Lakh')

class child2(child1):

    def money(self):
        child1.money(self)
        print('25Lakh')

c=child2()
c.money()
"""
#o/p--> 1CR
#           50Lakh
#           25Lakh

#Constructor overloading
"""
class grandpa:

     def __init__(self):
         print('500')

class father(grandpa):

    def __init__(self):
        super().__init__(self)
        print('300')

class child(father):

    def __init__(self):
        super().__init__(self)
        print('100')
g=grandpa()
print(dir(g))
"""
"""
class Institute:

    def Information(self,In,stack,fee):
        self.In=In
        self.stack=stack
        self.fee=fee

        print(f'The institute name is {self.In}')
        print(f'The stack courses  name is {self.stack} ')
        print(f'The total fee is {self.fee}')

class ClassStudent(Institute):

    def subinfo(self,sname,tclass,ttime):
        self.sname=sname
        self.tclass=tclass
        self.ttime=ttime

        print(f'The name of the subject is {self.sname}')
        print(f'The total class  is {self.tclass} ')
        print(f'The total  course duration is {self.ttime}')

class Result(ClassStudent):

    def finalstage(self,totalmarks,grade):
        self.total=totalmarks
        self.grade=grade

        print(f'The total marks are {self.totalmarks}')
        print(f'The total grade are {self.grade}')

r=Result()
r.Information("Qspider","Python full stack",65000)
r.subinfo("pyhton",10,'3hr')
r.finalstage(500,'A-Grade')
  """

class employee:

    def __init__(self,companyname,totalmember,highestpackage):
        self.name=companyname
        self.member=totalmember
        self.package=highesgtpackage
        self.data()

        def data(self):

            print(f'The company name is {self.companyname}')
            print(f'The total member in company are {self.totalmember}')
            print(f'The highestpackage of the employee is {self.highestpackage}')

class startemployee(employee):

    def __init__(self,sal,yop,roleyop):
        self.sal=sal
        self.yop=yop
        self.roleyop=roleyop
        self.info()


        def info(self):
            super().__init__('cognizant',25,'4LPA')
                print(f'The salary of the employee is {self.sal}')
                print(f'The year of experience of the employee is {self.yop}')
                print(f'The role of the employee is {self.roleyop}')

class  rules(startemployee):

    def __init__(self,intime,outtime,rolename):
        self.In=intime
        self.out=outtime
        self.role=rolename
        self.check()

        def  check(self):
            super().__init__(70000,2,'sde')
            print(f'The intime of the employee is {self.intime}')
            print(f'The outtime of the employee is {self.outtime} ')
            print(f'The role of the employee is {self.rolename}')
            
r=rules('11 am','6 pm','bussiness analyst')     
r.      















