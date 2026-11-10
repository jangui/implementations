
def main():
    max_int = 1000
    total = 0
    for i in range(1,max_int):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    print(total)

if __name__ == "__main__":
    main()
