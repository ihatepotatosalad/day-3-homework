def max_num(*x):
    return max(x)


def mult_list(*lst):
    if len(lst) == 0:
        return 0
    product = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            product = product * i
    return product


def rev_string(strng):
    return strng[::-1]


def num_within(x, a, b):
    return x in range(a, b + 1)


triangle = [[1], [1, 1]]


def pascal(x):
    if (x < 1):
        print('error')
    elif x == 1:
        print([0])
    else:
        row_number = 2
        while len(triangle) < x:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1]
                               [i - 1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)


pascal(5)
