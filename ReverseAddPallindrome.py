def reverse_and_add_palindrome(n: int, k: int):
    def is_palindrome(x):
        s = str(x)
        return s == s[::-1]

    for i in range(1, k+1):
        n = n + rev_n             
        if is_palindrome(n):
            return [i, n]          
    return [-1, -1]
