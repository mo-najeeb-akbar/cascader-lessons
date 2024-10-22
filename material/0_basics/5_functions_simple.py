
def add_one(x: int):
    return x + 1


def add(x: int, y: int):
    return x + y


def remove_from_list(x):
    x.pop(0)


if __name__ == "__main__":
    a = 1
    b = add_one(a)
    print(f'Result of add_one: {b}')

    var_0 = 1
    var_1 = 10
    var_2 = add(var_0, var_1)
    print(f'Result of add: {var_2}')

    my_list = [1, 2, 3]
    remove_from_list(my_list)
    print(f'Result of remove_from_list: {my_list}')
