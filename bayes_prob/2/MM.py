"""M&M豆问题
"""
from bayes_prob.lib.thinkbayes import Suite

mix94 = {
    'brown': 30,
    'yellow': 20,
    'red': 20,
    'green': 10,
    'orange': 10,
    'tan': 10
}

mix96 = {
    'blue': 24,
    'green': 20,
    'orange': 16,
    'yellow': 14,
    'red': 13,
    'brown': 13
}

# 假设 A B
hypoA = dict(bag1=mix94, bag2=mix96)
hypoB = dict(bag1=mix96, bag2=mix94)



class M_and_M(Suite):
    hypotheses = dict(A=hypoA, B=hypoB)
    def Likelihood(self, data, hypo):
        bag, color = data
        mix = self.hypotheses[hypo][bag]
        print(mix)
        like = mix[color]
        return like


suite = M_and_M('AB')

suite.Update(('bag1', 'yellow'))
# suite.Print()

suite.Update(('bag2', 'green'))
suite.Print()