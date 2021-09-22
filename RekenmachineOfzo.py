nummer1 = int(input('kies uw 1ste getal.\n'))
nummer2 = int(input('kies uw 2de getal.\n'))

plus = lambda a, b: a + b
print(plus(nummer1 , nummer2))

plus = lambda a, b: a * b
print(plus(nummer1 , nummer2))

plus = lambda a, b: a / b
print(plus(nummer1 , nummer2))

plus = lambda a : a + 1
print(plus(nummer1))

plus = lambda a : a - 1
print(plus(nummer1))