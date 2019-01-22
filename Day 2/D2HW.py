#Default Arguments

def greetings(name, msg = "Good morning!"):
   """   This function greets to the person with the provided message.
         If message is not provided, it defaults to "Good morning!"
   """
   print("Hello",name + ', ' + msg)

print("This is an example of Default Arguments:")
greetings("Black Widow")
greetings("Steve Rogers","How do you do?")


#Keyword Arguments

print("\n\nThis is an example of Keyword Arguments:")
greetings(msg = "How do you do?",name = "Bruce Banner")
greetings("Iron Man",msg = "How do you do?")


#Arbitrary Arguments or When number of inputs is not known

print("\n\nThis is an example of Arbitary Arguments:")
def greet(*names):
   """This function greets all the person in the names tuple."""
   # names is a tuple with arguments
   for name in names:
       print("Hello ",name)

greet("Natasha","Bruce","Steve","Tony")



#Anonymous/Lambda Function
print("\n\nThis is an example of Lambda Arguments:")
add=lambda x,y:x+y
print("Sum of 2 and 3 is ",add(2,3))
