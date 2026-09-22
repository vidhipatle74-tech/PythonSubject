"""
class company:
 
    name=cognizant

    def show_name(self):
        print(f'The name of the company is {self.name}')

class employee(company):

    types=regular

    def show_data1(self):
        print(f'The type of the company is {self.type}')

class employee2(employee):

    join_date=234

    def show_data2(self):
        print(f'The joining date of fthe employee is {self.join_date}')

e=employee()
e.show_data()
e.show_data1()
e.show_data2()
"""
#Hybrid inheritance==>>
"""
class flower:

    def show(self,name,smell):
        self.name=name
        self.smell=smell
        self.display()

    def display(self):
        print(f'The name of the flower is {self.name}')
        print(f'The smell of the flower is {self.smell}')

class jasmin(flower):

    def show1(self,color,species):
        flower.show(self,"marigold","mild")
        self.color=color
        self.species=species
        self.display1()

    def display1(self):
        print(f'The color of the flower is {self.color}')
        print(f'The species of the flower is {self.species}')

class rose(flower):

    def show2(self,shape, uses):
        self.shape=shape
        self.uses=uses
        self.display2()

    def display2(self):
        print(f'The shape of the flower is {self.shape}')
        print(f'The uses of the flower is {self.uses}')

class lily(jasmin,rose):

    def show3(self,environment,place):
        rose.show2(self,"oval","decoration")
        jasmin.show1(self,"pink","hybrid")
            
        self.environment=environment
        self.place=place
        self.display3()

    def display3(self):
        print(f'The place of the flower is {self.place}')
        print(f'The environment of the flower is {self.environment}')

l=lily()
l.show3('mositure','at home')

#o/p-->The shape of the flower is oval
#          The uses of the flower is decoration
#          The name of the flower is marigold
#          The smell of the flower is mild
#          The color of the flower is pink
#          The species of the flower is hybrid
#         The place of the flower is at home
#         The environment of the flower is mositure
"""

       
       


