def fib(series_len):
    if series_len == 1:
        return [0]

    fib_list = [0, 1]
    for ii in range(series_len-2):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list

def sum_fib(num_fib_elements):
    return sum(fib(num_fib_elements))


print(fib(4))
print(sum_fib(4))