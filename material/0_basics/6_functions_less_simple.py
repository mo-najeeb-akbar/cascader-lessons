
def add_basic(x, y):
    intermediate_var = x + y
    return intermediate_var


def add_less_basic(x, y):
    y = x + y
    return y


if __name__ == "__main__":

    var_0 = 1
    var_1 = 10
    var_2 = add_basic(var_0, var_1)
    print(f'Result of add_basic: {var_2}')
    # can i do this?
    # print(intermediate_var)

    var_3 = add_less_basic(var_0, var_1)
    print(f'Result of add_less_basic: {var_3}')
    print(f'Value of var_3 after application of add_less_basic: {var_1}')

    x = 100
    y = 200
    var_4 = add_less_basic(x, y)
    print(f'Result of add_less_basic: {var_4}')
    print(f'Value of y after application of add_less_basic: {y}')

