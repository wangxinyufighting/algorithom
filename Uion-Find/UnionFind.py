'''
并查集，用来检测一个图是否有环
检测的方法即是 找到一条额外的边，若边的两个顶点在同一个集合内，则有环。
若没有这样的边，则无环。
'''


#
def find_root(x, parent):
    x_root = x
    while parent[x_root] != -1:
        x_root = parent[x_root]

    return x_root

#x和y是一条边的两个顶点
#True: 合并失败，即x和y同属于一个集合，有环；False反之，无环
def union(x, y, parent):
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)

    if x_root != y_root:
        parent[x_root] = y_root
        return False
    else:
        return True

def unionWithCompress(x, y, parent, rank):
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)

    if x_root != y_root:
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        else:
            parent[x_root] = y_root
            rank[y_root] += 1
        return False
    else:
        return True

def initialize(nodeNums):
    parent = [-1] * nodeNums
    rank = [0] * nodeNums
    return parent, rank

if __name__ == '__main__':
    edges = [[0, 1], [1, 2], [1, 3], [3, 4], [2, 5], [2, 4]]
    parent, rank = initialize(6)
    cycle = False

    for i in range(len(edges)):
        x = edges[i][0]
        y = edges[i][1]

        if unionWithCompress(x, y, parent, rank):
            cycle = True
            break

    if cycle:
        print('yes')
    else:
        print('no')