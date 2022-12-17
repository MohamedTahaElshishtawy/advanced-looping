def sumOfDigitsFrom1ToN(n):
    result = 0

    for x in range(1, n+1):
        result = result + sumOfDigits(x)

    if result%n == 0:
        print("The sum is divisible")
        for x in range(1, n + 1):
            if x != n:
                print(f"{x} + ", end='')
            else:
                print(f"{x} = ", end='')
        return result
    else:
        print("The sum is not divisible")
        return 0

def sumOfDigits(x):
    sum = 0
    while (x != 0):
        sum = sum + x % 10
        x = x // 10

    return sum


n = int(input("Enter your number: "))
print(sumOfDigitsFrom1ToN(n))