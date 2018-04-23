from bayes_prob.lib.thinkbayes import MakeGaussianPmf, Suite, EvalPoissonPmf, Pmf, MakePoissonPmf, MakeMixture,MakeExponentialPmf,\
    PmfProbLess
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

class Hockey(Suite):

    def __init__(self, name):
        pmf = MakeGaussianPmf(2.7, 0.3, 4)
        super(Hockey, self).__init__(pmf, name)


    def Likelihood(self, data, hypo):
        lam = hypo
        k = data
        like = EvalPoissonPmf(k, lam)
        return like

suite1 = Hockey('bruins')
suite1.UpdateSet([0, 2, 8, 4])

suite2 = Hockey('canucks')
suite2.UpdateSet([1, 3, 1, 0])



def draw(suite, color, label):
    X, Y = [], []
    [(X.append(x), Y.append(y)) for x, y in sorted(suite.Items())]
    plt.plot(X, Y, color=color, linewidth=1.0, linestyle="-", label=label)
    plt.legend(loc='upper right')


draw(suite1, 'blue', 'bruins')
draw(suite2, 'red', 'canucks')
plt.title(u'每场比赛进球数后验分布', fontsize=20)
plt.show()


def MakeGoalPmf(suite):
    metapmf = Pmf()

    for lam, prob in suite.Items():
        pmf = MakePoissonPmf(lam, 10, name=lam)
        metapmf.Set(pmf, prob)
    mix = MakeMixture(metapmf)
    return mix


mix1 = MakeGoalPmf(suite1)
mix2 = MakeGoalPmf(suite2)


draw(mix1, 'blue', 'bruins')
draw(mix2, 'red', 'canucks')
plt.title(u'每场比赛进球数后验分布', fontsize=20)
plt.show()

diff = mix1 - mix2

p_win = diff.ProbGreater(0)
p_loss = diff.ProbLess(0)
p_tie = diff.Prob(0)

print('p_win:', p_win)
print('p_loss:', p_loss)
print('p_tie', p_tie)

def MakeGoalTimePmf(suite):
    metapmf = Pmf()

    for lam, prob in suite.Items():
        pmf = MakeExponentialPmf(lam, high=2, n=2001)
        metapmf.Set(pmf, prob)
    mix = MakeMixture(metapmf)
    return mix

time_dist1 = MakeGoalTimePmf(suite1)
time_dist2 = MakeGoalTimePmf(suite2)

draw(time_dist1, 'blue', 'bruins')
draw(time_dist1, 'red', 'canucks')
plt.title(u'两次得分间的间隔时间分布', fontsize=20)
plt.show()

p_overtime = PmfProbLess(time_dist1, time_dist2)
print(p_overtime)

p_win = diff.ProbGreater(0) + p_tie*p_overtime

print("棕熊队赢的概率:", p_win)