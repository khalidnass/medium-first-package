def all_prime_numbers(n):
    if not type(n) is int or n <= 1:
        return []
    else:
        for div in range(2,n+1):
            if n % div == 0:
                return [div] + all_prime_numbers(n//div)