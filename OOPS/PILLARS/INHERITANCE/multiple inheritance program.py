class hotel:

    def __init__(self,hname,harea,hpincode):
        self.name=hname
        self.area=harea
        self.pincode=hpincode
        self.Address()

    def Address(self):
        print(f'The name of the hotel is {self.name}')
        print(f'The area of the hotel is {self.area}')
        print(f'The pincode of the hotel area  is {self.pincode}')

class customer:

    def __init__(self,cname,tmember,tbill,ordernum):

        self.name=cname
        self.member=tmember
        self.bill=tbill
        self.num=ordernum
        self.show_data()

    def show_data(self):
        print(f'The name of the customer is {self.name}')
        print(f'The total member is {self.member}')
        print(f'The total bill of the customer is {self.bill}')
        print(f'The order number of the customer is {self.num} ')

class review(hotel,customer):

    def __init__(self,rating,tipbill):
        super().__init__("joy","pune",441911)
        customer.__init__(self,"abhi",5,6000,"b1234")
        self.rating=rating
        self.bill=tipbill
        self.show_data1()

    def show_data1(self):
        print(f'The rating of the hotel is {self.rating}')
        print(f'The tip of the bill is {self.bill}')

r=review("5**** rating",200)


#o/p--> The name of the hotel is joy
#           The area of the hotel is pune
#           The pincode of the hotel area  is 441911
#           The name of the customer is abhi
#           The total member is 5
#           The total bill of the customer is 6000
#           The order number of the customer is b1234 
#           The rating of the hotel is 5**** rating
#          The tip of the bill is 200

        
