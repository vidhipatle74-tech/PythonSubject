#import os
#print(os.getcwd())
#os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")
#file=open("done.txt",'w+')
#file.write("class completed")
#print(file.tell())
#print(file.seek(3))


import os
print(os.getcwd())
os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")
with open("vidhi.txt",'a')as file:
    file.write("i am the greatest one ")
    #file.write("god bless me")
    #file.writelines(["12345 \n","abcde \n"])

os.popen("vidhi.txt")
