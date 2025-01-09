# n, a = map(int, input().split())
# t = list(map(int, input().split()))
n, a = 3, 3
t = [1, 4, 7]

if __name__ == "__main__":
    print(n, a)
    print(t)
    end_time = 0
    for i in range(n):
        if (t[i] + a) > end_time + a:
            end_time = t[i] + a
        else:
            end_time += a
        print(end_time)
