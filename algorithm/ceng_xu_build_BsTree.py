class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def creatTree(nodeList):
    if nodeList[0] == '#':
        return None
    head = Node(nodeList[0])
    que = [head]
    j = 1
    for node in que:
        if node != None:
            node.left = (Node(nodeList[j]) if nodeList[j] != '#' else None)
            que.append(node.left)
            j += 1
            if j == len(nodeList):
                return head
            node.right = (Node(nodeList[j]) if nodeList[j] != '#' else None)
            j += 1
            que.append(node.right)
            if j == len(nodeList):
                return head


def hou_xu(root):
    global res
    if root == None:
        return
    hou_xu(root.left)
    hou_xu(root.right)
    res.append(root.val)


if __name__ == '__main__':
    lis = '123#45'
    root = creatTree(lis)
    res = []
    hou_xu(root)
    print(res)
