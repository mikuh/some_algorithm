"""
小明每天晚上会做这三件事中的一件:{吃饭,睡觉,打豆豆},而具体会做哪件事情取决于当天的天气情况,
天气情况分为{晴天,雨天}两种,每天只会是晴天或是雨天的一种,如果是晴天,那么小明[吃饭,睡觉,打豆豆]的概率分别是[0.6, 0.3, 0.1];
而如果是雨天,小明[吃饭,睡觉,打豆豆]的概率分别是[0.1,0.4,0.5]. 同样天气的变化也遵循一定的概率,
晴天转雨天的概率是0.4,晴天继续保持晴天的概率是0.6,而雨天转晴天的概率是0.3,
雨天继续保持雨天的概率是0.7.现已知某连续的三天小明做的事情是[吃饭,睡觉,打豆豆],那么请问这三天最有可能的天气情况序列是?
"""

states = ('雨天', '晴天')

observations = ('吃饭', '睡觉', '打豆豆')

transition_probability = {
    '雨天': {'雨天': 0.7, '晴天': 0.3},
    '晴天': {'雨天': 0.4, '晴天': 0.6},
}

# 这个是根据transition_probability 求极限得到稳态的状态概率
start_probability = {'雨天': 0.57, '晴天': 0.43}

emission_probability = {
    '雨天': {'吃饭': 0.1, '睡觉': 0.4, '打豆豆': 0.5},
    '晴天': {'吃饭': 0.6, '睡觉': 0.3, '打豆豆': 0.1},
}


def viterbi2(obs, states, start_p, trans_p, emit_p):
    V = [{} for _ in range(len(obs))]
    path = {}
    # t = 0
    for state in states:
        path[state] = [state]
        V[0][state] = start_p[state] * emit_p[state][obs[0]]
    # t > 1
    for t in range(1, len(obs)):
        new_path = {}
        for state in states:
            V[t][state], last_state = max(
                (V[t - 1][last_state] * trans_p[last_state][state] * emit_p[state][obs[t]], last_state)
                for last_state in V[t - 1])
            new_path[state] = path[last_state] + [state]
        path = new_path
    max_pro, max_state = max((V[-1][state], state) for state in V[-1])
    return path[max_state], max_pro


if __name__ == '__main__':
    p, pro = viterbi2(['吃饭', '睡觉', '打豆豆'], states, start_probability, transition_probability,
                      emission_probability)
    print(p, pro)
