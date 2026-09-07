"""class bank:
    def total_balance(self):
        self.amount=50000
        print(f'the total_balance is {self.amount}')
    def Deposit(self):
        self.dep=2000
        total_amount=total_amount+balance
        print(f'the balance after deposite is{self.balance}')
        

    def withdraw(self):
        self.withd=5000
        total_amount=total_Amount-balance
        print(f'the balance after wuthdraw is {self.balance}')
s=bank()
s.total_balance()
s.Deposit()
s.withdraw()
"""


class flipkart:
    product_name="phone"
    cost="100000"
    total_product=5
    address="pune"

    def product_data(self):
        print(f'product name is {self.product_name}')
        print(f'total cost is {self.cost}')
        print(f'total product is {self.total_product}')

    def address(self):
        print(f'The current address is {self.address}')

    def modification_data(self,new_cost,total_product):
        self.cost=new_cost
        self.total_product=total_product
        print(f'updated cost is {self.new_cost}')
        print(f'updated total_product is{self.total_product}')
        
f=flipkart()
f.product_data()
f.address()
f.modification_data(75000,10)
f.cost()
f.total_product()
