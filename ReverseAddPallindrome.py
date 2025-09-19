n = int(input())
k = int(Input())

for i in range(1, k+1):
    rev_n = int(str(n)[::-1])   # reverse the digits
    n = n + rev_n               # add reversed number
    s = str(n)
    if s == s[::-1]:            # check palindrome
        print([i, n])
        break
else:
    print([-1, -1])


