def input_int_numbers():
    while True:
        try:
            return tuple(map(int,  input().split()))
        except ValueError as ex:
            print(ex)
        else:
            break


if __name__ == "__main__":
    result = input_int_numbers()
    print(*result)
