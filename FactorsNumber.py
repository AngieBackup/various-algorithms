def compute_factors(number):
    factors = []

    if number > 1:
        factors.append(1)

    limit = number // 2 + 1
    divisor = 2

    while divisor < limit: # Curent divisor hasn't been evaluated. Mientras no se ha terminado de evaluar cada número entre number / 2.
      quotient = number // divisor
      divisor_is_divisible_by_number = number == divisor * quotient
      
      if divisor_is_divisible_by_number:
        factors.append(divisor)
        quotient_hasnt_been_evaluated = divisor < quotient # At this point quotient is a divisible number candidate

        if quotient_hasnt_been_evaluated:
          factors.append(quotient)

        limit = quotient - 1 # Is always divisor + 1

      divisor += 1

    return factors