input("left shift double, right shift half. Press Enter to continue...")
print(" 3 << 1 =", 3 << 1, " 12 >> 1 =", 12 >> 1)
print(" 3 << 2 =", 3 << 2, " 12 >> 2 =", 12 >> 2)

n = int(input("enter a number ( try 5 or 8): "))
guess = input("what is " + str(n) + " << 2? ")
input("left shift by 2 multiplies by 4. press enter to continue...")
print(" ", n, "<< 2 =", n << 2, "your guess:", guess )