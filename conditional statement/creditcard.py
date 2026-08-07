#8.wap to give 10% off only who is purchasing in credit card and min 3 product should purchase
#and each product price should be more than 500.

#Nested if-else

# payment-mode-> cc,gpay,ppay,csd

#mode-> user->enter payment mode

#cc-> 10%when-> min 3product price>500



paymentMode=["credit card",'Gpay','ppay','cod']

mode=eval(input("Enter payment mode:"))


if mode in paymentMode:  

    print(f"you choose {mode}")

    totalproduct=eval(input("Enter total product:"))

    if totalproduct>=3:

        print(f"you have total product {totalproduct}")

        p1=eval(input("Enter p1 amount:"))
        p2=eval(input("Enter p2 amount:"))
        p3=eval(input("Enter p3 amount:"))


        if p1>=500 and p2>=500 and p3>=500:

            if mode==paymentMode[0]:

                print("Congratulation | you got 10% discount on credit card")

                #discount logic 10%

                total = p1+p2+p3
                discount= total*10/100
                final_amt= total-discount

                print("Total amt:",total)
                print("Discount :",discount)
                print("Final amount is :",final_amt)

            else:
                
                print(f"you choose {mode} so you not get 10% discount")


        else:
            print("total product price is not greater than 500")

    else:
        print("you don't have total product greater than 3")

else:
    print("Invalid payment mode")
                

        
