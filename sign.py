input("XOR sign detection - n ^ < 0 means different signs. Press Enter to continue...")
print(" 4 ^ 2 =", 4 ^ 2,  "same signs positive")
print(" 4 ^ -2 =", 4 ^ -2, "different signs negative")

n = int(input("enter a number ( try 3 or -7): "))
guess = input("will " + str(n) + " ^ -8 be positive or negative? ")
input("XOR is negative when the signs are different. press enter to continue...")
print(" ", n, "^ -8 =", n ^ -8, "your guess:", guess )