
            #STRING FORMATING:

#there are three types of string formating:

#(1)formating with placeholder

#here we can't replace the data

#EXAMPLE:

x="My name is %s & my age is %d"%('vidhi',21)   #var_name=""%()
print(x)

#--> my name is vidhi and my age is 21

#(2).formating

#here we can replace the data

#EXAMPLE:

x="I wanna go somewhere{}".format('manali')      #var_name="".format()
print(x)

#--> i wanna go somewhere manali

#(3)formating with literals

#RULES:

#-->{}
#-->Inside the braces we have to pass variables     #->{python}
#-->before the quotes we have to mention either f/F    F--> if you want to insert

#EXAMPLE:

x="vidhi"
y= 21

msg=f'my name is {x} & my age is {y}'
print(msg)

#--> my name is vidhi & my age is 21


#FORMATING WITH PLACEHOLFDER:

#(1) %S-->for string datatype
#(2) %d-->for integer datatype
#(3) %f-->for float datatype
#(4) %2f--> it will consider after (.) if it will take 2 digit 
#(5) %1f--> after (.) it will consider 1 digit




