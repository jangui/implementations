
def main():
    max_int = 931000
    total = 0
    for i in range(1, max_int+1):
        if i % 2 != 0:
            print(i)
            total += i**2

    print(total)


if __name__ == "__main__":
    main()
