paymentMode=["gpay","fampay","creditcard","ppay"]

mode=eval(input("enter the payment mode"))

if mode in paymentMode:
    print(f"You choose {mode} mode")

    totalproduct=eval(input("enter the  Total_product"))

    if totalproduct>=3:
        print("you have total {product} product")

        product1=eval(input("enter the amount"))
        product2=eval(input("enter the amount"))
        product3=eval(input("enter the amount"))


        if product1>=500 and product2>=500 and product3>=500:
            

            if mode==paymentMode[2]:
                print("you will get 10%  of discount")

                total_amount=product1+product2+product3
                discount=total_amount*10/100
                final_amount=total_amount-discount
                print('total_amount:',total_amount)
                print('total_discount:',discount)
                print('final_amount:',final_amount)
                
            else:
                print("you will not get any kind of discount")

        else:
            print("you will not get  any discount")

    else:
        print("you dont have more than 3 products")

else:
    print("invalid mode")
