from bayes_prob.lib.thinkbayes import Suite, Pmf, MakeJoint, MakeHistFromDict
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签


class Die(Suite):
    def __init__(self, sides):
        super(Die, self).__init__(self)
        for x in range(1, sides +1):
            self.Set(x, 1)
        self.Normalize()


d6 = Die(6)
d8 = Die(8)

mix = Pmf()
for die in [d6, d8]:
    for val, prob in die.Items():
        mix.Incr(val, prob)

mix.Normalize()
# print(mix.d)

dies = {4:Die(4), 6:Die(6), 8:Die(8), 12:Die(12), 20:Die(20)}
pmf_dice = Pmf()
pmf_dice.Set(4, 2)
pmf_dice.Set(6, 3)
pmf_dice.Set(8, 2)
pmf_dice.Set(12, 1)
pmf_dice.Set(20, 1)
pmf_dice.Normalize()
print(pmf_dice.GetDict())

mix = Pmf()
for die_key, weight in pmf_dice.Items():
    for outcome, prob in dies[die_key].Items():
        mix.Incr(outcome, weight * prob)

X = []
Y = []
[(X.append(x), Y.append(y)) for x, y in mix.Items()]
plt.bar(range(len(X)), Y, tick_label=X, label=u'混合分布')
plt.legend(loc='upper right')
plt.show()

