
if __name__ == "__main__":

    a = 15

    # simple condition

    if a < 10:
        print('Hello, world!')
    else:
        print('Ope! Not big enough.')

    b = 42.0

    # chained condition

    if 0.0 <= b <= 50.0:
        print('b is in range')

    # compound condition
    if a < 10 and b > 20:
        print('Happy!')
    else:
        print('Sad!')

    # can even use expressions

    if 2*a+b < 500.0:
        print('OOOO')
