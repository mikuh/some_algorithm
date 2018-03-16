"""
随机抽题只告诉正确数，怎么获取全部答案？
100道题，每次随机抽取12题，每题三个选项，答题后只知道对了几题，不限答题次数，请问如何快速获得每道题的正确答案？
问题来源：https://www.zhihu.com/question/268775851
"""
import numpy as np
# 初始化问题及答案及选择得分
question_num = 100
extraction_num = 12
options = ['A', 'B', 'C']
action_num = len(options)
id2answer = [np.random.choice(options) for _ in range(question_num)]
id2value = [np.zeros(action_num) for _ in range(question_num)]
threshold = extraction_num / action_num

def value(ids):
    trues = 0
    choices = [(_id, np.argmax(id2value[_id])) for _id in ids]
    for id, a, in choices:
        if options[a] == id2answer[id]:
            trues += 1
    return choices, trues

def policy_improvement(ids):
    choices, trues = value(ids)
    if trues == extraction_num:
        for _id, a in choices:
            id2value[_id] = [0]*action_num
            id2value[_id][a] += 100000000000000
    else:
        for _id, a in choices:
            for i in range(3):
                if i != a:
                    id2value[_id][i] -= (trues - threshold) * threshold
                else:
                    id2value[_id][i] += trues - threshold
    return value(ids)

if __name__ == '__main__':
    curr_acc = 0
    flag = 0
    for n in range(1000000):
        ids = np.random.choice(list(range(question_num)), extraction_num)
        _, trues = policy_improvement(ids)
        result = [options[np.argmax(x)] for x in id2value]
        accuracy = np.sum([y1 == y2 for y1, y2 in zip(id2answer, result)]) / question_num
        flag += 1
        if accuracy > curr_acc:
            flag = 0
            print()
            print("当前阈值:", threshold)
            print("正确答案：", id2answer)
            print("当前答案：", result)
            print("第{}次正确率：{}".format(n, accuracy))
            curr_acc = accuracy
        if flag > question_num * extraction_num and threshold <= extraction_num:
            threshold += 1
        if accuracy == 1.0:
            break
