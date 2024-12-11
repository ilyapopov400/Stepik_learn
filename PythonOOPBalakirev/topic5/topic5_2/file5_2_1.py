a = input().split()

if __name__ == "__main__":
    result = None
    try:
        result = sum(map(lambda x: int(x), a))
    except ValueError:
        try:
            result = sum(map(lambda x: float(x), a))
        except ValueError:
            try:
                result = ''.join(a)
            except:
                pass
    finally:
        print(result)
