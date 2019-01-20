spam=input()

if (spam == '1'):
    print("Hello") #1 is stored in spam
elif (spam=='2'):
    print("Howdy") #2 is stored in spam
else:
    print("Greetings! ")


(5 > 4) and (3 == 5)  # False
not (5 > 4)  # False
(5 > 4) or (3 == 5)  # True
not ((5 > 4) or (3 == 5))  # False
(True and True) and (True == False)  # False
(not False) or (not True)  # True
