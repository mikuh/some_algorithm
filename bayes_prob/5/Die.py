from bayes_prob.lib.thinkbayes import Suite, SampleSum
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
class Die(Suite):
    def __init__(self, sides):
        super().__init__(self)
        for x in range(1, sides +1):
            self.Set(x, 1)
        self.Normalize()

d6 = Die(6)
dice = [d6] * 3
three = SampleSum(dice, 1000)


three_exact = d6 + d6 + d6
three_exact.Print()

X1, Y1, X2, Y2 = [], [], [], []
for x, y in sorted(three.Items()):
    X1.append(x)
    Y1.append(y)

for x, y in sorted(three_exact.Items()):
    X2.append(x)
    Y2.append(y)

plt.plot(X1, Y1, color="blue", linewidth=1.0, linestyle="-", label=u'模拟')
plt.plot(X2, Y2, color="red", linewidth=1.0, linestyle="-", label=u'枚举')
plt.legend(loc='upper right')
plt.show()