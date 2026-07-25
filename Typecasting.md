**------------------------------------------------------------------------------------------------**

**# What is Typecasting in python?**

**-------------------------------------------------------------------------------------------------**

**-->>Typecasting means changing one data type into another data type.**



**-->In Python, sometimes we need to convert data from one type to another so that we can perform different operations.**



**-->Typecasting is the process of converting the value of one data type into another data type.**



**## For example:**



**-->Converting a string to an integer**

**-->Converting an integer to a float**

**-->Converting a float to a string**



**---------------------------------------------------------------------------------------------------**

**##-Why is Typecasting Needed?**

**---------------------------------------------------------------------------------------------------**

**Typecasting is useful because different data types behave differently.**



**-->For example:**



**a = "10"**

**b = "20"**



**print(a + b)**



**Output:**



**1020**



**-->Here, Python joins the two strings instead of adding the numbers.**



**-->To perform addition, convert them to integers.**



**a = int("10")**

**b = int("20")**



**print(a + b)**



**Output**



**30**



**---------------------------------------------------------------------------------------------------**

**#Types of Typecasting**

**---------------------------------------------------------------------------------------------------**

**There are two types of typecasting in Python.**



**#1. Implicit Typecasting (Automatic)**



**Python automatically converts one data type into another whenever it is safe.**



**Example**

**a = 10**

**b = 2.5**



**print(a + b)**



**Output**



**12.5**



**-->>Explanation**



**a is an integer.**

**b is a float.**

**Python automatically converts 10 into 10.0.**

**Then it performs the addition.**



**This automatic conversion is called Implicit Typecasting.**



**#2. Explicit Typecasting (Manual)**

**---------------------------------------------------------------------------------------------------**

**In explicit typecasting, the programmer converts the data type manually using built-in functions.**



**Python provides many functions for this.**



**Common Typecasting Functions:**



###### **#1. int()**

###### **----------**

**Converts a value into an integer.**



**Example**

**a = "25"**



**b = int(a)**



**print(b)**

**print(type(b))**



**Output**



**25**

**<class 'int'>**





###### **#2. float()**

**--------------**

**Converts a value into a floating-point number.**



**Example**

**a = 15**



**b = float(a)**



**print(b)**



**Output**



**15.0**



###### **#3. str()**

**------------**

**Converts a value into a string.**



**Example**

**a = 100**



**b = str(a)**



**print(type(b))**



**Output**



**<class 'str'>**



###### **#4. bool()**

**-------------**

**Converts a value into Boolean (True or False).**



**-Example**

**print(bool(1))**

**print(bool(0))**

**print(bool(""))**

**print(bool("Python"))**



**Output**



**-True**

**False**

**False**

**True**

**Rule**

**0 → False**

**Empty string "" → False**

**Empty list \[] → False**

**Everything else → True**



###### **#5. list()**

**-------------**

**Converts data into a list.**



**Example**

**a = (1, 2, 3)**



**b = list(a)**



**print(b)**



**Output**



**\[1, 2, 3]**



###### **#6. tuple()**

###### **------------**

**Converts data into a tuple.**



**Example**

**a = \[10, 20, 30]**



**b = tuple(a)**



**print(b)**



**Output**



**(10, 20, 30)**



###### **#7. set()**

**-----------**

**Converts data into a set.**



**Example**

**a = \[1, 2, 2, 3, 3]**



**print(set(a))**



**Output**



**{1, 2, 3}**



**-->Duplicate values are removed because a set stores only unique elements.**

**-----------------------------------------------------------------------------------------------**

&#x20;       **#Typecasting Table:**

**-----------------------------------------------------------------------------------------------**



**Function	Converts To	         Example**

&#x20;   **|               |                       |**

**int()	        Integer          	int("10") → 10**

**float()	        Float	                float(5) → 5.0**

**str()	        String           	str(100) → "100"**

**bool()	        Boolean          	bool(0) → False**

**list()	        List	                list((1,2)) → \[1,2]**

**tuple()	        Tuple	                tuple(\[1,2]) → (1,2)**

**set()	         Set	                set(\[1,1,2]) → {1,2}**



**-------------------------------------------------------------------------------------------------**

**-->Real-Life Example**

**-------------------------------------------------------------------------------------------------**

**Imagine you are filling an online form.**



**Your age is entered as "20" (text).**

**The computer cannot calculate with text.**

**It converts "20" into the number 20.**

**Now it can perform calculations.**



**This conversion is similar to typecasting.**

**---------------------------------------------------------------------------------------------------**

**#Advantages of Typecasting:**

**---------------------------------------------------------------------------------------------------**

**-->Makes different data types compatible.**

**-->Helps perform mathematical calculations.**

**-->Makes programs flexible.**

**-->Allows conversion between different data types.**

**-->Reduces type-related errors.**

**-->Important Points to Remember**

**-->Python is a dynamically typed language.**

**-->Implicit typecasting is done automatically by Python.**

**-->Explicit typecasting is done by the programmer using functions like int(), float(), and str().**

**Not every conversion is valid.** 

