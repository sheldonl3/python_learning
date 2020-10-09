#反转满二叉树的某一棵子树
def rev_tree(input):
    if len(input) != 2:
        return 0
    l = 2 ** a1[0] - 1
    print(l)
    tree = [i + 1 for i in range(l)]
    print(tree)
    reve(tree, input[1] - 1, 0)
    print(tree)


def reve(tree, index, jie):
    l = len(tree)
    left = index * 2 + 1
    right = left + 2 ** jie
    print(index, left, right, jie)
    if left > l or right > l - 1:
        return
    else:
        for i in range(2 ** jie):
            tree[left + i], tree[left + i + 2 ** jie] = tree[left + i + 2 ** jie], tree[left + i]
        reve(tree, left, jie + 1)


if __name__ == '__main__':
    a = input().split()
    a1 = []
    for k in a:
        a1.append(int(k))
    rev_tree(a1)
