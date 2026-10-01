input("XOR swap - exchange two values without a third variable. Press Enter to continue...")
print(" before: a = 5, b = 10")
a, b = 5, 10
a ^=b; b ^= a; a ^= b
print(" after: a=", a, " b =", b)
n = int(input("enter a number ( try 3 or 7): "))
guess = input("after XOR swap" + str(n) + " and 8 what does n become? ")
a, b = n, 8
a ^= b; b ^= a; a ^= b
input("XOR swap - exchange the value. press enter to continue...")
print(" n became:", a, "your guess:", guess )