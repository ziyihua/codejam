from typing import List, Tuple


Printer = Tuple[int, int, int, int] # (c, m, y, k)


def print_letters(printers: List[Printer]) -> str:
    '''
    Returns the minimum number of letters that can be printed with the given printers.
    '''
    # Find the minimum number of each color
    min_colors = [min([printer[i] for printer in printers]) for i in range(4)]
    total_used = 0
    for i in range(4):
        total_used += min_colors[i]
        if total_used > 10**6:
            # If the total number of colors used is greater than 10**6,
            # subtract the difference from the current color
            min_colors[i] -= total_used - 10**6
            total_used = 10**6

    # Check if the total number of colors used is less than 10**6
    if sum(min_colors) < 10**6:
        return "IMPOSSIBLE"
    else:
        return " ".join(str(color) for color in min_colors)


def main() -> None:
    testcases = int(input())
    for i in range(testcases):
        printers = []
        for j in range(3):
            printers.append(tuple(int(ink) for ink in input().split()))
        print(f"Case #{i+1}: " + print_letters(printers))

if __name__ == "__main__":
    main()