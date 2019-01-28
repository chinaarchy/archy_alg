def sqrt(num, threshold):
    low, high = 0, num
    while True:
        mid = (low + high) / 2
        sqr = mid ** 2

        if abs(sqr - num) <= threshold:
            break
        elif sqr > num:
            high = mid
        else:
            low = mid

    return mid


if __name__ == "__main__":
    print("%.6f" % sqrt(2, 10e-6))
