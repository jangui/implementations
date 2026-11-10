def sumFactors(max_int, factor):
    """
    sum of the factors = factor * sum(1+2+3+...+ largest_factor)
    sum(1+2+...+ largest_factor) = (largest_factor)(largest+factor+1) / 2
    sum of factors = factor * ((largest_factor)(largest+factor+1) / 2)
    """
    largest_factor = max_int // factor
    total = factor * ((largest_factor)*(largest_factor+1)/2)
    return total

def main():
    max_int = 999
    solution = sumFactors(999, 3) + sumFactors(999, 5) - sumFactors(999,15)
    print(solution)

if __name__ == "__main__":
    main()
