def print_pyramid():
    h = input("Enter the height of the pyramid: ")

    height = int(h)

    for i in range(1, height + 1):
        s = " " * (height - i)
        styars = "*" * (2 * i - 1)
        print(s + y)

print_pyramid()
