x = input("Please input an integer: ")
x = int(x)
for i in range(1, x+1):
     nums = range(1, i+1)
     print(' + '.join(map(str, nums)), '=', sum(nums))