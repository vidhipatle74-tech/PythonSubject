class dad:
    cash=10000
    
    def villa(self):
        print(f"Dad's villa")

class child(dad):
    bike_name="bmw"

    def home(self):
        print(f"dad's gift")



    
d=dad()
d.villa()
d.home()
print(d.cash)
print(d.bike_name)
