import Dice
from bayes_prob.lib.thinkbayes import Percentile
import matplotlib.pyplot as plt
class Train(Dice.Dice):
    def __init__(self, hypos, alpha=1.0):
        """ 通过秘律函数初始化概率"""
        super().__init__(self)
        for hypo in hypos:
            self.Set(hypo, hypo**(-alpha))
        self.Normalize()


hypos = range(1, 501)
suite = Train(hypos)
suite.Update(60)
suite.Update(30)
suite.Update(90)
suite.Print()


X = [x for x, _ in suite.Items()]
Y = [y for _, y in suite.Items()]

plt.plot(X, Y)
plt.show()

def Mean(suite):
    """后验分布 列车数量的期望
    """
    total = 0
    for hypo, prob in suite.Items():
        total += hypo*prob
    return total

print(Mean(suite))


interval = Percentile(suite, 5), Percentile(suite, 95)
print(interval)