import util

if __name__ == "__main__":
    sub = list(map(int, input("Enter list values (space-separated): ").split()))

    A = set(map(int, input("Enter set A values (space-separated): ").split()))

    B = set(map(int, input("Enter set B values (space-separated): ").split()))

    total = util.Sets(sub, A, B)

    print("Total:", total)
