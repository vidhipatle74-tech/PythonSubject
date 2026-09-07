#Accessing the class variable inside the  class method ==>>
"""
class Qspiders:
    Trainer_name="prabhu sir"

    @classmethod
    def show_data(cls):
        print(f'The name of the Qspider Trainer is {cls.Trainer_name}')
Qspiders.show_data()
"""
#o/p-->  The name of the Qspider Trainer is prabhu sir
#After accessing class variable inside the class method ===>>
#Modification  in class-variable using two way-->
#(1)-> using classname
#(2)-> using object

#(1)-> using classname
"""
class flight:
    flight_number="DH145"

    @classmethod
    def show_data(cls):
        print(f'The flight number is {flight.flight_number}')
        #modification
        flight.flight_number="MH123"
        print(f'The updated flight_number is {flight.flight_number}')
flight.show_data()
"""
#o/p--> The flight number is DH145
#            The updated flight_number is MH123

#--> by using object-->

class Train:
    train_coach="s2"

    @classmethod
    def data(cls):
        print(f'The train coach is {T.train_coach}')
       
T=Train()
T.train_coach="B1"
print(f'The updated train coach is {T.train_coach}')
T.data()






