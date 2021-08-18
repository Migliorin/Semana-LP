#print(2 == 2.0) # True
#print(2 != 2.0) # False
#print(2 == 2.1) # False

#print(25>= 25) # True
#print(25>25) # False

#print(15 = 15) # Erro, nao e possivel

#print(not (2 == 2.0)) # True -> False
#print(not (2 == 2.1)) # False -> True

print((2 == 2.0) and (2 == 2.1)) # True and False - > False
print((2 == 2.1) and (2 == 2.1)) # False and False -> False
print((2 == 2.0) and (2 == 2.0)) # True and True -> True
print("")
print((2 == 2.0) or (2 == 2.1)) # True and False - > True
print((2 == 2.1) or (2 == 2.1)) # False and False -> False
print((2 == 2.0) or (2 == 2.0)) # True and True -> True
