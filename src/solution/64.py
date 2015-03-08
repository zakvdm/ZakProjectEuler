f = open('64.txt', 'r')
input = f.read()

def populateTree(values):
    strings = ''.join(values).splitlines()
    print(strings[0])
    print(strings[-1])
    tree = [[(int(cell), 0) for cell in row.split(' ')] for row in strings]

    # Set the values for the bottom row:
    tree[-1] = [(node[0], node[0]) for node in tree[-1]]

    for y in range(2, len(tree) + 1):
        treeIndex = y * -1
        for i in range(0, len(tree[treeIndex])):
            nodeVal = tree[treeIndex][i][0]
            leftChild = tree[treeIndex + 1][i][1]
            rightChild = tree[treeIndex + 1][i + 1][1]
            val = (nodeVal, nodeVal + max(leftChild, rightChild))
            tree[treeIndex][i] = val

    return tree

tree = populateTree(input)

print(tree[0])
#for row in tree:
#    print(row)

