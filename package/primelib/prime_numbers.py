def prime_numbers(n):
    if not type(n) is int or n <= 1:
        return []
    else:
        for div in range(2,n+1):
            if n % div == 0:
                return [div] + prime_numbers(n//div)