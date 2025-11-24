name = 'saurabh' # this is valid
# for = "student"   this line is not run because for is key word
print(name)
# print(for) # this is invalid

# False      await      else       import     pass  
# None       break      except     in         raise  
# True       class      finally    is         return  
# and        continue   for        lambda     try  
# as         def        from       nonlocal   while  
# assert     del        global     not        with  
# async      elif       if         or         yield

"""
💡 Notes:

These words can’t be used as variable names or identifiers.

They’re reserved by Python because they define the syntax and structure of the language.

You can check them directly in Python using this command: 
"""
import keyword
print(keyword.kwlist)
