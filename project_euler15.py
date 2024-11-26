#!/bin/python3


def main():
    max_col = 20
    max_row = 20
    nodes = {}
    for row in range(0, max_row+1):
        for col in range(0, max_col+1):
            nodes[row, col] = Node(None, None)

    for row in range(0, max_row):
        for col in range(0, max_col):
            if row < max_row:
                nodes[row, col].right = nodes[row+1, col]
            if col < max_col:
                nodes[row, col].down = nodes[row, col+1]

    for layer in range(1, max_row+1):
        node_layer = []
        root_node = nodes[max_row-layer, max_col-layer]
        curr_node = root_node
        while curr_node.right:
            node_layer.append(curr_node)
            curr_node = curr_node.right
        curr_node = root_node
        while curr_node.down:
            curr_node = curr_node.down
            node_layer.append(curr_node)

        for node in node_layer:
            queue = []
            # top_node = nodes[max_row-layer, max_col-layer]
            top_node = node
            queue.append(top_node)
            count = 0
            while queue:
                node = queue.pop(0)
                if node.paths_found:
                    count += node.paths_found
                    print(node.paths_found)
                    print(count)
                else:
                    if node.right:
                        queue.append(node.right)
                    if node.down:
                        queue.append(node.down)
                    if not node.right and not node.down:
                        count += 1
            top_node.paths_found = count
        print(max_row-layer, max_col-layer, count)
    print(nodes[0, 0].paths_found)



class Node():
    def __init__(self, right, down, paths_found=None):
        self.right = right
        self.down = down
        self.paths_found = paths_found


if __name__ == '__main__':
    main()
