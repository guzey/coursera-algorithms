import math

inversions = 0


def merge_sort(x):
    global inversions

    if len(x) == 1:
        return x
    else:
        left = x[:math.ceil(len(x) / 2)]
        right = x[math.ceil(len(x) / 2):]
        temp_left = merge_sort(left)
        temp_right = merge_sort(right)

    temp = []
    i = 0
    j = 0
    for n in range(0, len(x)):
        if i == len(temp_left):
            temp.extend([temp_right[j]])
            j += 1
        elif j == len(temp_right):
            temp.extend([temp_left[i]])
            i += 1
        elif temp_left[i] < temp_right[j]:
            temp.extend([temp_left[i]])
            i += 1
        else:
            temp.extend([temp_right[j]])
            j += 1
            inversions += len(left) - i

    return temp


def main():
    # a test case from coursera forums
    nums = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12,
            13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]

    merge_sort(nums)
    print(inversions)


if __name__ == "__main__":
    main()
