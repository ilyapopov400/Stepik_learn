def get_loss(w1: (int, float), w2: (int, float), w3: (int, float), w4: (int, float)):
    try:
        return 10 * w1 // w2 - 5 * w2 * w3 + w4
    except ZeroDivisionError as z:
        return "деление на ноль"
    else:
        return - (5 * w2 * w3 + w4)


if __name__ == "__main__":
    a = get_loss(1, 0, 3, 4)
    print(a)
