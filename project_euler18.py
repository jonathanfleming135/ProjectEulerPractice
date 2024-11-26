#!/bin/python3


def main():
    tree = [
                            [75],
                          [95, 64],
                        [17, 47, 82],
                      [18, 35, 87, 10],
                     [20, 4, 82, 47, 65],
                    [19, 1, 23, 75, 3, 34],
                  [88, 2, 77, 73, 7, 63, 67],
                [99, 65, 4, 28, 6, 16, 70, 92],
              [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
          [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
      [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]

    tree_nodes = {}
    for i in range(len(tree)):
        row = tree[i]
        for j, val in enumerate(row):
            node = Node(None, None, val)
            tree_nodes[i, j] = node

        if i-1 >= 0:
            row_above = tree[i-1]
            for j in range(len(row_above)):
                node_above = tree_nodes[i-1, j]
                node_above.left = tree_nodes[i, j]
                node_above.right = tree_nodes[i, j+1]

    queue = []
    queue.append(tree_nodes[0,0])
    total_max = 0
    while queue:
        node = queue.pop(0)
        node_total_val = node.val + node.max_sum

        if node.left:
            if node_total_val > node.left.max_sum:
                node.left.max_sum = node_total_val
            if not node.left.traversed:
                queue.append(node.left)

        if node.right:
            if node_total_val > node.right.max_sum:
                node.right.max_sum = node_total_val
            if not node.right.traversed:
                queue.append(node.right)

        if node_total_val > total_max:
            total_max = node_total_val
        node.traversed = True

    print(total_max)




class Node():
    def __init__(self, left, right, val: int, max_sum=0, traversed=False):
        self.left = left
        self.right = right
        self.val = val
        self.traversed = traversed
        self.max_sum = max_sum

    # # try greedy algorithm...
    # Greedy algorithm didn't work :(
    # sum = 0
    # prev_pos = 0
    # for row in tree:
    #     left = row[prev_pos]

    #     try:
    #         right = row[prev_pos+1]
    #     except IndexError:
    #         right = 0

    #     next_val = max(left, right)
    #     if next_val == right:
    #         prev_pos += 1
    #     sum += next_val
    #     print(next_val)

    # print(sum)

if __name__ == '__main__':
    main()
