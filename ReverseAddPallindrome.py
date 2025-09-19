n = int(input())
k = int(input())

for i in range(1, k+1):
    n = n + int(str(n)[::-1])   # add reverse
    if str(n) == str(n)[::-1]:  # check palindrome
        print([i, n])
        break
else:
    print([-1, -1])

