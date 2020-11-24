from FactorsNumber import get_sum_factor

def print_friend_numbers_in_range(start, end):
  serie = range(start, end)
  
  for a in serie:
    sum1 = get_sum_factor(a)# Sum of the factors of a number

    for b in serie:
      sum2 = get_sum_factor(b) # Sum of the factors of b number
      is_a_friend_number = sum1 == b and sum2 == a and a != b

      if is_a_friend_number:
        print(f"Friends: a: {a}, b: {b}")

n = 3
start, end = 10**(n-1), 10**n
print_friend_numbers_in_range(start, end)