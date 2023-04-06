def print_punched_card(r: int, c: int) -> None:
    '''
    Prints a punched card with r rows and c columns. 
    '''
    boundary = '+-' * c + '+'
    cells = '|.' * c + '|'
    for row in range(r):
        if row == 0:
            print('..'+boundary[2:])
            print('..'+cells[2:])
        else:
            print(boundary)
            print(cells)
    print(boundary)


def main() -> None:
    '''
    Reads the number of test cases and the number of rows and columns for each test case.
    '''
    testcases = int(input())
    for i in range(testcases):
        print("Case #{}:".format(i + 1))
        r, c = input().split()
        r, c = int(r), int(c)
        print_punched_card(r, c)


if __name__ == "__main__":
    '''
    Calls the main function.
    '''
    main()
