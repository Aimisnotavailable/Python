
x = int(input("Enter first num: "))
y = int(input("Enter second num: "))

lcm_x = x
lcm_y = y

while(y != 0):
    rem = x % y
    x = y
    y = rem
gcd = x
lcm = int((lcm_x * lcm_y)/gcd)

print("GCF IS : ",x)
print("LCM IS : ", lcm)