def bus_A(T, A, hours_v, minutes_v):
    result = 0
    for x in range(480, T + A, A):
        hours_b1, minutes_b1 = divmod(x, 60)
        if hours_b1 * 60 + minutes_b1 > 1320:
            return -1
        elif hours_b1 * 60 + minutes_b1 >= 1320 == (hours_v * 60 + minutes_v) >= 1320:
            result = abs(((hours_b1 - hours_v) * 60) + (minutes_b1 - minutes_v))
            return result
        result = abs(((hours_b1 - hours_v) * 60) + (minutes_b1 - minutes_v))
    return result


def bus_B(T, B, hours_v, minutes_v):
    result = 0
    for y in range(480, T + B, B):
        hours_b2, minutes_b2 = divmod(y, 60)
        if hours_b2 * 60 + minutes_b2 > 1320:
            return -1
        elif hours_b2 * 60 + minutes_b2 >= 1320 == (hours_v * 60 + minutes_v) >= 1320:
            result = abs(((hours_b2 - hours_v) * 60) + (minutes_b2 - minutes_v))
            return result
        result = abs(((hours_b2 - hours_v) * 60) + (minutes_b2 - minutes_v))
    return result


def wait_time(H, M, A, B):
    T = H * 60 + M
    hours_v, minutes_v = divmod(T, 60)
    time_A = bus_A(T, A, hours_v, minutes_v)
    time_B = bus_B(T, B, hours_v, minutes_v)

    if time_A == -1 or time_B == -1:
        return max(time_A, time_B)
    else:
        return min(time_A, time_B)


def main():
    H = int(input())
    M = int(input())
    A = int(input())
    B = int(input())

    result = wait_time(H, M, A, B)

    print(result)  # Для человека
    return result  # Для программы


main()
