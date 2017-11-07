"""
很久以前写的n杯倒水问题
"""


from itertools import product
from copy import deepcopy

class Node(object):
    def __init__(self, status, pre=None):
        self.status = status
        self.pre = pre


def get_steps(cup_volume, water, objective, deepth):
    operation = [(x, y) for x, y in product(list(range(len(cup_volume))), repeat=2) if x != y]
    cup_status = [0]*(len(cup_volume))
    if water > sum(cup_volume):
        raise "水太多装不下了啦"
    for i, volume in enumerate(cup_volume):
        if water <= 0:
            break
        if water <= volume:
            cup_status[i] = water
            water = 0
        else:
            cup_status[i] = volume
            water -= volume
    head = Node(cup_status)
    status_set = {str(cup_status)}
    status_record = [[head]] + [[]]*deepth
    for i in range(deepth):
        for node in status_record[i]:
            cup_status = node.status
            for x, y in operation:
                next_cup_status = deepcopy(cup_status)
                residue_water = cup_volume[y] - cup_status[y]
                if cup_status[x] >= residue_water:
                    next_cup_status[x] = cup_status[x] - residue_water
                    next_cup_status[y] = cup_volume[y]
                else:
                    next_cup_status[y] = cup_status[y] + cup_status[x]
                    next_cup_status[x] = 0
                cur_node = Node(next_cup_status, pre=node)
                if objective in next_cup_status:
                    return cur_node
                if str(next_cup_status) not in status_set:
                    status_record[i+1].append(cur_node)
                    status_set.add(str(next_cup_status))
    return False


def find_method(cup_volume, water, objective, deepth):
    last_node = get_steps(cup_volume, water, objective, deepth)
    if last_node:
        result = []
        p = last_node
        while True:
            cup_status = p.status
            result.append(cup_status)
            p = p.pre
            if p is None:
                break
        print(result[::-1])
    else:
        print('{}步内无解'.format(deepth))


find_method([10, 5, 6], 11, 8, 10)