from bayes_prob.lib.thinkbayes import Suite
import matplotlib.pyplot as plt

class Train(Suite):
    def Likelihood(self, data, hypo):
        if hypo < data:
            return 0
        else:
            return 1 / hypo

hypos = list(range(1, 501))
suite = Train(hypos)

suite.Update(60)
# suite.Print()




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