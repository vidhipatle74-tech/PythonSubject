#(1)--> tell()-->
#                     -->if we want to know the cursor point (where the cursor is present) then
#                            we can go for tell ()

#                    --->it wont accepts anything

#(2)--> seek()-->

#      it will give the information , if you want to go for navigation then we can go for
#       seek () function

#       it will accepts 1 argument


import os
print(os.getcwd())
os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")
file=open("dell.txt",'w')

