class Solution:  # chaoshi a
    def __init__(self):
        self.tmp_max_height = 0

    def findMinHeightTrees(self, n: int, edges):
        m = len(edges)
        if m == 0:
            return [0]
        leave = []
        root = []
        res = []
        min_height = 65535
        if m == 1:
            root = edges[0]
        else:
            for i in range(m):
                for j in range(2):
                    # print(edges[i][j])
                    if edges[i][j] not in leave and edges[i][j] not in root:
                        leave.append(edges[i][j])
                    elif edges[i][j] in leave:
                        root.append(edges[i][j])
                        leave.remove(edges[i][j])

        def find_height(root, edges, leave, height):
            # tmp_max_height = 0
            # print(root)
            if root in leave:
                return height
            for i in range(len(edges)):
                if root in edges[i]:
                    if root == edges[i][0]:
                        tmp = find_height(edges[i][1], edges[:i] + edges[i + 1:], leave, height + 1)
                    else:
                        tmp = find_height(edges[i][0], edges[:i] + edges[i + 1:], leave, height + 1)
                    if tmp > self.tmp_max_height:
                        self.tmp_max_height = tmp
            return self.tmp_max_height

        # print('leave=', leave)
        # print('root=', root)
        for each in root:
            h = find_height(each, edges, leave, 0)
            self.tmp_max_height = 0
            # print(each, h)
            if h == min_height:
                res.append(each)
            elif h < min_height:
                res.clear()
                res.append(each)
                min_height = h

        print('res=', res)
        return res


class Solution2():          #拓扑排序，先删除外围节点，留下中心的是结果 = 剥洋葱
    def findMinHeightTrees(self, n: int, edges):
        m = len(edges)
        if m == 0:
            return [0]
        dp = [[] for _ in range(n)]
        for i in range(n - 1):
            dp[edges[i][0]].append(edges[i][1])
            dp[edges[i][1]].append(edges[i][0])
        print(dp)
        depue = []
        for i in range(len(dp)):
            if len(dp[i]) == 1:
                depue.append(i)
        total = 0
        while depue:
            print('dp', dp)
            print('dep', depue)
            print()
            l = len(depue)
            total += l
            if total == n:    #最后一层就是结果
                return depue
            for i in range(l):
                #print(i)
                dp[dp[depue[i]][0]].remove(depue[i])
                if len(dp[dp[depue[i]][0]]) == 1:
                    depue.append(dp[depue[i]][0])
            depue = depue[l:]


if __name__ == '__main__':
    s = Solution2()
    print(s.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
