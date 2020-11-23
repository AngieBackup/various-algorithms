def compute_divisors(number):
    divisors = []
    start_point = number // 2 + 1
    
    for n in range(start_point - 1, 0, -1):
        is_divisible = number % n == 0

        # print(f"n: {n}")
        if is_divisible == True:
            print(f"is_divisible: {n}")
            divisors.append(n)

    return divisors