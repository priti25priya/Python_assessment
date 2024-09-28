
from util import find_unique_numbers


def main():
    my_list = [1, 2, 3, 4, 5, 3, 2, 1, 6, 7]
    unique_values = find_unique_numbers(my_list)
    print("Unique values:", unique_values)


if __name__ == "__main__":
    main()
