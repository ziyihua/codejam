from typing import List


def chain_reactions(weights: List[int], edges: List[int]):
    total = 0
    # having_fun stores the live value excluding the current node, and the dead values of all other branches
    having_fun = [[0, 0] for _ in range(len(weights))]
    non_initiators = set(edges)
    for node in range(len(weights)-1, -1, -1):
        if node not in non_initiators:
            having_fun[node] = [weights[node], 0]
        target = edges[node]
        if target == -1:
            total += max(having_fun[node][0], weights[node]) + having_fun[node][1]
        elif having_fun[target][0] == 0:
            assert having_fun[target][1] == 0
            having_fun[target][0] = max(having_fun[node][0], weights[node])
            having_fun[target][1] = having_fun[node][1]
        else:
            current_live = max(having_fun[node][0], weights[node])
            if current_live > having_fun[target][0]:
                having_fun[target][1] += (current_live + having_fun[node][1])
            else:
                having_fun[target][1] += having_fun[target][0] + having_fun[node][1]
                having_fun[target][0] = current_live
    return total


def main() -> None:
    testcases = int(input())
    for i in range(testcases):
        count_nodes = int(input())
        weights = [int(n) for n in input().split()]
        edges = [int(n)-1 for n in input().split()]
        print(f"Case #{i+1}: {chain_reactions(weights, edges)}")


def main_from_file():
    results = []
    with open('test_data/test_set_3/ts3_input.txt') as f:
        testcases = int(f.readline())
        for i in range(testcases):
            count_nodes = int(f.readline())
            weights = [int(n) for n in f.readline().split()]
            edges = [int(n)-1 for n in f.readline().split()]
            results.append(f"Case #{i+1}: {chain_reactions(weights, edges)}")
            
    with open('test_data/test_set_3/ts3_output.txt') as f:
        for i, line in enumerate(f):
                if line.rstrip() != results[i]:
                    print(f"Test case {i+1} failed: {line.rstrip()} != {results[i]}")


if __name__ == "__main__":
    main()