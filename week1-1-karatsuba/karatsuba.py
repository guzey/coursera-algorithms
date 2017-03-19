import math


def karatsuba(x, y):
    digits_x = str(x)
    digits_y = str(y)
    len_x = len(digits_x)
    len_y = len(digits_y)

    if len_x == 1 or len_y == 1:
        return int(x) * int(y)
    else:
        a = digits_x[0:int(len_x / 2)]
        b = digits_x[int(len_x / 2):]
        c = digits_y[0:int(len_y / 2)]
        d = digits_y[int(len_y / 2):]
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        a_b_c_d = karatsuba(int(a) + int(b), int(c) + int(d))

        first = (10 ** (len_x + len_y - len(a) - len(c))) * int(ac)
        second = (10 ** (math.ceil(len_x / 2))) * (a_b_c_d - int(ac) - int(bd))
        third = int(bd)

        return first + second + third


def main():
    num_1 = 12223555
    num_2 = 11333275

    print(karatsuba(num_1, num_2))
    print(num_1 * num_2)


if __name__ == "__main__":
    main()
