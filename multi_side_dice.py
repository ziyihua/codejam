from typing import List


def longest_straight(numbers: List[int]) -> int:
    numbers.sort()
    current = 1
    for num in numbers:
        if num >= current:
            current += 1
    return current - 1


def main() -> None:
    testcases = int(input())
    for i in range(testcases):
        count_dices = int(input())
        dices = [int(n) for n in input().split()]
        print(f"Case #{i+1}: {longest_straight(dices)}")


if __name__ == "__main__":
    main()
