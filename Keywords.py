
               #KEYWORDS:
 
 #Keywords are  the fixed words, pre-defined words or preserved words  which has some special meaning is called keywords.

 #there are 35 keywords in pyhton programming language.

 #THREE keywords are special :
                            True
                            False
                            None

 
#These are special beacuse the first letter of these keywords are in uppercase.
                          
                            AND

# We can assign these keywords as a value to a variables.

# we cannot assiagn any value to a keywords, except (True,False,None)



#IMPORT KEYWORD IN GROUP FORMAT:
 
           help('keywords')
 
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 


#IMPORT KEYWORS IN LIST FORMATE:

                                 import keyword
                                 keyword.kwlist
-->>>>
import keyword
keyword.kwlist

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#TO CHECK WHETHER THE KEYWORD IS VALID OR NOT :
              
                                              import keyword
                                              keyword.iskeyword()




>>>import keyword
   keyword.iskeyword('True')

   True
(where,True is a keyword thats why the ans is true).




