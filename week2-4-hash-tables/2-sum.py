sums_to_check = []


# checks if there exists a pair of distinct numbers in numbers that sum to current_sum
def two_sum_search(numbers):
    i = 0
    for current_sum in sums_to_check:
        for number in numbers:
            if current_sum - number in numbers and current_sum - number != number:
                i += 1
                break
    return i


def main():
    global sums_to_check

    numbers_list = 'nums.txt'

    with open(numbers_list) as file:
        numbers = []
        for line in file:
            numbers.extend(line.split())

        numbers = {int(i): 0 for i in numbers}

    print('numbers done')

    sums_to_check = list(range(-10000, 10001))
    print(two_sum_search(numbers))


if __name__ == "__main__":
    main()
