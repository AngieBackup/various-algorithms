from FactorsNumber import compute_factors

def get_sum(factors):
  sum = 0

  for factor in factors:
    sum = sum + factor

  return sum

def print_friend_numbers_in_range(start, end):
  serie = range(start, end)
  for a in serie:
    a_factors = compute_factors(a)
    sum1 = get_sum(a_factors)# Sum of the factors of a number

    for b in serie:
      b_factors = compute_factors(b)
      sum2 = get_sum(b_factors) # Sum of the factors of b number
      is_a_friend_number = sum1 == b and sum2 == a

      if is_a_friend_number:
        print(f"Friends: a: {a}, b: {b}")

n = 3
start, end = 10**(n-1), 10**n
print_friend_numbers_in_range(start, end)