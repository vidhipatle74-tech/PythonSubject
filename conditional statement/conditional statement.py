#WAP to build a simple menu-driven food ordering system. Accept a menu number from the user and
#display the corresponding food item along with its price. If the entered menu number is invalid,
#print "Invalid Menu".

#WAP to check the teacher's mood based on the percentage of assignments submitted by the class.
#Conditions:If 100% of the assignments are submitted, print "Teacher is Very Happy ".
#Else if the percentage is between 75% and 99%, print "Teacher is Happy".
#Else if the percentage is between 50% and 74%, print "Teacher is Angry   ".
#Otherwise (below 50%), print "Surprise Test Tomorrow!  "

percentage=eval(input("enter the number"))
assignment=eval(input("enter the percentage"))

if percentage==100:
    print("teacher is very happy")

elif 75<=percentage<=99:
    print("Teacher is happy")

elif 50<=percentage<=74:
    print("Teacher is angry")

else:
    print("Surprise test tomorrow")



#WAP to suggest a weekend plan based on the user's money and mobile battery percentage.

#Money ≥ ₹1000 and Battery ≥ 80% → Go on a Trip 🏖️
#Money ≥ ₹500 and Battery ≥ 50% → Watch a Movie 🍿
#Money ≥ ₹200 and Battery ≥ 20% → Go to a Café ☕
#Otherwise → Stay Home and Study Python 🐍

'''battery=eval(input("enter the percentage"))
money=eval(input("enter the money"))

if money>=1000 and battery>=80:
    print("go on a trip")

elif money>=500 and battery>=50:
    print("watch a movie")

elif money>=200 and battey>=20:
    print("go to a cafe")

else:
    print("stay home and study python")'''
