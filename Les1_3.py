x = int(input("введите число:"))
xstart = x
num = x % 10
biggist = num
while x > 0:
    digit = x % 10
    if digit > num:
        biggist = digit
    x = x // 10
    print(x)
print(f"в числе {xstart} самая большая цифра {biggist}")





