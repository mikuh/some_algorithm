"""
狄克斯特拉算法实现
原理应该就是改造了一下广度优先搜索算法
先写个递归实现，感觉只会写递归了orz 感觉循环的写法好麻烦..
"""


def get_path(node, parents, path):
    node = parents[node]
    path = node + '->' + path
    if node == 'start':
        return path
    return get_path(node, parents, path)


def dijkstras(node, costs, parents):
    for sub_node in graph[node]:
        cost = costs[node] + graph[node][sub_node]
        if sub_node not in costs or costs[sub_node] > cost:
            parents[sub_node] = node
            costs[sub_node] = cost
    for node in graph[node]:
        dijkstras(node, costs, parents)


if __name__ == '__main__':
    """
    写个例子
    """
    infinity = float("inf")  # 无穷大

    # 图
    graph = {}

    # 起始点
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    # A点
    graph["a"] = {}
    graph["a"]["fin"] = 1
    # B点
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    # 终点
    graph["fin"] = {}

    # 节点开销散列表
    costs = {}

    # 初始化
    costs['start'] = 0
    costs['a'] = infinity
    costs['b'] = infinity
    costs['fin'] = infinity
    # 父节点
    parents = {}
    dijkstras("start", costs, parents)
    path = get_path('fin', parents, 'fin')
    print("节点开销：", costs)
    print("最小路径：", path)
