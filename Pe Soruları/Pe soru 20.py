import math
hundredfactorial = math.factorial(100)
hundredfactorial = str(hundredfactorial)
number = 0
for i in hundredfactorial:
    number += int(i)
print(number)
