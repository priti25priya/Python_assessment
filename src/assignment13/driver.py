
import util

if __name__ == "__main__":
    x, y = map(int, input("Enter numbers (x y): ").split())
    matrix = [list(map(int, input().split())) for _ in range(x)]

    total = util.find_max_and_min(x, y, matrix)
    print("Max of min values:", total)
