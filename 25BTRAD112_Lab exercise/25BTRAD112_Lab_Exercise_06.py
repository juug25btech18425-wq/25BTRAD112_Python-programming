# Lab Exercise 6: Prime number and factorial programs
n = int(input("Enter a number: "))

# Prime Number
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# Factorial
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)
