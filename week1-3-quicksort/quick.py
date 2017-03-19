import math


def median_of_three(three):
    if three[2] < three[0] < three[1]:
        return three[0]
    elif three[1] < three[0] < three[2]:
        return three[0]
    elif three[2] < three[1] < three[0]:
        return three[1]
    elif three[0] < three[1] < three[2]:
        return three[1]
    else:
        return three[2]


# I removed the the stuff that was only needed to submit the problem set but has no relation to the algorithm itself
def quick(x):
    if len(x) <= 1:
        return x
    else:
        three = [x[0], x[math.ceil(len(x) / 2) - 1], x[len(x) - 1]]
        pivot_element = x.index(median_of_three(three))
        p = x[pivot_element]
        i = 1
        j = i
        # switch pivot element in the first place so could iterate well
        x[pivot_element] = x[0]
        x[0] = p
        for j in range(i, len(x)):
            if x[j] < p:
                temp = x[i]
                x[i] = x[j]
                x[j] = temp
                i += 1
        temp = x[0]
        x[0] = x[i - 1]
        x[i - 1] = temp

        x[0:i - 1] = quick(x[0:i - 1])
        x[i:len(x)] = quick(x[i:len(x)])

        return x


def main():

    nums = [5, 3, 4, 2, 6, 1, 7, 8, 9]

    print(quick(nums))


if __name__ == "__main__":
    main()
