import heapq


# this function assumes that all provided numbers are distinct
def calculate_sum_of_medians(numbers):
    smalls = []
    bigs = []
    count = 0
    sum_of_medians = 0
    for number in numbers:
        # first, we need to make sure there's at least one number in each heap, before starting the main algorithm
        # in order to be able to push new numbers to the right heaps

        # if bigs is empty, insert the number to bigs
        if not bigs:
            heapq.heappush(bigs, number)

        # if smalls is empty
        elif not smalls:
            # and if the new number is small, then insert it to smalls
            # not that the values in smalls are inverted to allow for extract max operation
            if number < bigs[0]:
                heapq.heappush(smalls, -number)
            # else switch the other number to the smalls and insert the new one to the bigs
            else:
                heapq.heappush(smalls, -heapq.heappop(bigs))
                heapq.heappush(bigs, number)

        # if both heaps aren't empty, then
        else:
            # if the number is bigger than the smallest in bigs, insert to bigs
            if number > bigs[0]:
                if len(bigs) <= len(smalls):
                    heapq.heappush(bigs, number)
                else:
                    heapq.heappush(smalls, -heapq.heappop(bigs))
                    heapq.heappush(bigs, number)
            # if the number is smaller than the biggest in smalls, insert to smalls
            elif number < -smalls[0]:
                if len(smalls) <= len(bigs):
                    heapq.heappush(smalls, -number)
                else:
                    heapq.heappush(bigs, -heapq.heappop(smalls))
                    heapq.heappush(smalls, -number)
            # To reduce the amount of numbers switching heaps, in edge cases, insert to the shorter heap
            # strictly speaking, only the first two (second modified from elif to else) clauses would do the job.
            else:
                if len(bigs) <= len(smalls):
                    heapq.heappush(bigs, number)
                else:
                    heapq.heappush(smalls, -number)

        count += 1
        # if the current number of elements looked at is odd and the middle element is in bigs
        if count % 2 == 1 and len(bigs) > len(smalls):
            # then assign median from bigs
            median = bigs[0]
        # in other cases, i.e. middle element is in smalls or we looked at an even number of elements)
        else:
            # assign median from smalls
            median = -smalls[0]
        sum_of_medians += median
        # print(smalls, bigs)

    return sum_of_medians


def main():
    # numbers_list = 'median.txt'
    #
    # with open(numbers_list) as file:
    #     numbers = []
    #     for line in file:
    #         numbers.extend(line.split())
    #
    #     numbers = [int(x) for x in numbers]

    numbers = [5, 3, 6, 9, 1, 2, 8, 7, 4]

    print(calculate_sum_of_medians(numbers))


if __name__ == "__main__":
    main()
