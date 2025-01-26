def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        prime = True
        if result <= 1:
            prime = False
        elif result == 2:
            prime =  True
        elif result % 2 == 0:
            prime = False
        else:
            for i in range(3, int(result ** 0.5) + 1, 2):
                if result % i == 0:
                    prime = False
        if prime:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)

print(result)