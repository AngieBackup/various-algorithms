from FactorsNumber import get_sum_factor


def is_perfect_number(start, end):
    serie = range(start, end)
   
    for number in serie:
        a_sum_factors = get_sum_factor(number)

        if number == a_sum_factors:
            print(f"Perfect Number: number: {number}")


n = 2
start, end = 10**(n-1), 10**n
is_perfect_number(start, end)