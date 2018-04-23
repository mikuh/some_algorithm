"""
选择A
"""
from bayes_prob.lib.thinkbayes import Suite

class Monty(Suite):
    def Likelihood(self, data, hypo):
        """如果奖品在A后面，那么打开另外两个其中一个的概率是0.5
        如果奖品在某个后面，那么打开这个的概率为0，另一个是1
        """
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1


suite = Monty('ABC')
suite.Update('B')
suite.Print()