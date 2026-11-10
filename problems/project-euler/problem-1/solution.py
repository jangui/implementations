def sumFactors(max_int, factor):
    return sum(range(1, (max_int // factor) + 1)) * factor

def main():
    max_int = 999
    solution = sumFactors(999, 3) + sumFactors(999, 5) - sumFactors(999,15)
    print(solution)

if __name__ == "__main__":
    main()
