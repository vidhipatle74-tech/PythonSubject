import csv
print(os.getcwd())
os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")
with open("RCB.txt",'w', newline="") as file:
    x=csv.writer(file)
    x.writerows([["name","sub","rating"]],[["A","py","*"]],[["B","SQL","1.5"]])

os.popen("RCB.csv")
